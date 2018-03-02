
import threading
import thread
import types
import time
import logging

class DoMaths:
	def __init__(self):
		self.num = 0
		self._lock = threading.Lock()

	def dosquare(self):
		with self._lock:
			# logging.debug('Starting')
			self.num+=1
			time.sleep(0.1)
			self.num = self.num * self.num
			# logging.debug('Exiting')

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
Exit ***********  1 thread number 1
Enter ***********  1 thread number 1
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




















