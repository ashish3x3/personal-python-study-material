
import threading
import thread
import types
import time
import logging


'''

The reason for this is that decorators are applied at the time the class is defined, not at the point at which it is instanced. Before it is instanced python has no idea that self.lock actually exists. Because of this we have to give the name as a string and rely on the fact that it will accurately find the correct member once the class is instanced. this will be seen in decorating all method with sync


outer_lock = threading.Lock()
Worth nothing that as this class instance lock is created at run-time we need an outer lock, created before anything in the instance, to ensure there is no race condition with who gets to create the first class instance lock (imagine two threads calling this method for the first time, at the same time). For this we create an outer lock at the time of class definition (when the decorator is applied) and use this to ensure only one instance lock is created.

problem is Each of our methods uses a different lock.
In Java method synchronization all synchronization methods refer to the same object instance lock.

The second thing to notice is that I'm now using an RLock instead of a normal lock. This is a re-entrant lock and allows a thread to call acquire on a lock more than once if it already holds the lock.

This ensures that if a method calls another method internally it will not cause deadlock as a thread tries to acquire a lock it already owns. In fact we might have wanted to use an RLock for our previous method decorator - otherwise recursion would cause a deadlock.

'''
# http://theorangeduck.com/page/synchronized-python

def synchronized(func):

	outer_lock = threading.Lock()

	def sync_with_attr(self, *args, **kwargs):
		with outer_lock:
			if not hasattr(self, '_lock'):
				# both works self._lock & setattr
				self._lock = threading.Lock()
				# setattr(self, '_lock', threading.Lock())
			lock = getattr(self, '_lock')
			with lock:
				return func(self, *args, **kwargs)
	return sync_with_attr

class DoMaths:
	def __init__(self):
		self.num = 0
		# self._lock = threading.Lock()

	@synchronized
	def dosquare(self):
		self.num+=1
		time.sleep(0.1)
		self.num = self.num * self.num

	def counter(self):
		for i in range(3):
			print 'Enter *********** ',self.num,threading.current_thread().getName()
			self.dosquare()
			print 'Exit *********** ',self.num,threading.current_thread().getName()




ist  = DoMaths()
# print ist.dosquare()
# print ist.dosquare()


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


This new decorator basically checks if the class instance already has a lock for the method to use. If a lock exists it uses it, otherwise it creates a new one and attaches it to the instance. Worth nothing that as this class instance lock is created at run-time we need an outer lock, created before anything in the instance, to ensure there is no race condition with who gets to create the first class instance lock (imagine two threads calling this method for the first time, at the same time). For this we create an outer lock at the time of class definition (when the decorator is applied) and use this to ensure only one instance lock is created.
'''














