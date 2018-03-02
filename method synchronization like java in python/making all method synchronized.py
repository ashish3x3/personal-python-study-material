
import threading
import thread
import types
import time
import logging

'''
The reason for this is that decorators are applied at the time the class is defined, not at the point at which it is instanced. Before it is instanced python has no idea that self.lock actually exists. Because of this we have to give the name as a string and rely on the fact that it will accurately find the correct member once the class is instanced.

The second thing to notice is that I'm now using an RLock instead of a normal lock. This is a re-entrant lock and allows a thread to call acquire on a lock more than once if it already holds the lock.

This ensures that if a method calls another method internally it will not cause deadlock as a thread tries to acquire a lock it already owns. In fact we might have wanted to use an RLock for our previous method decorator - otherwise recursion would cause a deadlock.

Finally if we take a look at our decorator synchronized_with_attr we realize this isn't a decorator in itself, but in fact a function which returns a decorator. This is a key aspect of how we argument decorators and begins to show their full power.

'''
# http://theorangeduck.com/page/synchronized-python


def synchronized_with_lockname(lock_name):

	def synchronized(func):

		def sync_with_attr(self, *args, **kwargs):
			_lock = getattr(self, lock_name)
			with _lock:
				return func(self, *args, **kwargs)

		return sync_with_attr

	return synchronized

class DoMaths:
	def __init__(self):
		self.num = 0
		self._lock = threading.RLock()

	@synchronized_with_lockname('_lock')
	def dosquare(self):
		self.num+=1
		time.sleep(0.1)
		self.num = self.num * self.num

	"""if U don't define RLock, line 41 will cause deadlock becasue the thread will again try to call lock.acquire() on an already acquired lock. RLock allow U to call lock.acqauire() on an already acquired lock more than once. and the execution won't halt, otherwise it will hault after entering thread number 1. Though line 41 is not required as the function it is calling is already under thread sync  """

	@synchronized_with_lockname('_lock')
	def counter(self):
		for i in range(3):
			print 'Enter *********** ',self.num,threading.current_thread().getName()
			self.dosquare()
			print 'Exit *********** ',self.num,threading.current_thread().getName()

ist  = DoMaths()

thread1 = threading.Thread(target = ist.counter)
thread2 = threading.Thread(target = ist.counter)

thread1.setName("thread number 1" )
thread2.setName("thread number 2" )

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print ist.num

'''
Enter ***********  0 thread number 1
Enter ***********  1 thread number 2
Exit ***********  2 thread number 1
Enter ***********  2 thread number 1
Exit ***********  5 thread number 2
Enter ***********  5 thread number 2
Exit ***********  26 thread number 1
Enter ***********  26 thread number 1
Exit ***********  677 thread number 2
Enter ***********  677 thread number 2
Exit ***********  458330 thread number 1
Exit ***********  210066388900 thread number 2
210066388900
'''





