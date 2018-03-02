
import threading,thread
import time
import types

# http://theorangeduck.com/page/synchronized-python

''''
Sometimes we wish to lock over all of the methods for a class. Creating what is essentially a thread safe data structure. In Java this is easy - we just add the synchronized keyword to the class definition.
public synchronized class Counter { }

'''

def sync_with_lock_name(lock_name):

	def decorator(func):
		def sync_with_attr(self, *args, **kwargs):
			_lock = getattr(self, lock_name)
			with _lock:
				return sync_with_attr(self, *args, **kwargs)
		return sync_with_attr
	return decorator

def sync_with_lock(lock):

	# This method could sync a  function and a class, depending on its type
	def sync_obj(obj):

		# if this decorator is called only for a specfic function, this will run
		if type(obj) is types.FunctionType:
			obj.__lock__ = lock

			def func(*args, **kwargs):
				with lock:
					obj(*args, **kwargs)
			return func

		# if this decorator is called for a class, this will run
		elif type(obj) is types.ClassType:
			orig_init = obj.__init__
			def __init__(self,*args, **kwargs):
				self.__lock__ = lock
				orig_init(self,*args, **kwargs)
			obj.__init__ = __init__

			for key in obj.__dict__:
				val = obj.__dict__[key]
				if type(val) is types.FunctionType:
					decorator = sync_with_lock(lock)
					obj.__dict__[key] = decorator(val)

			return obj

	return sync_obj


def synchronized(lock):
	# if type of lock is a lock name instead of a lock itself. call sync_with_lock_name
	if type(lock) is types.StringTypes:
		decorator = sync_with_lock_name(lock)
		return decorator(lock)

	# if lock type is a lock itself
	if type(lock) is thread.LockType:
		decorator = sync_with_lock(lock)
		return decorator(lock)

	else:
		new_lock = threading.RLock()
		decorator = sync_with_lock(new_lock)
		return decorator(lock)



@synchronized
class Counter:
	def __init__(self):
		self.counter = 0

	def add_one(self):
		val = self.counter
		val += 1
		time.sleep(0.1)
		self.counter = val
		print '#### ',self.counter, threading.current_thread().getName()

	def add_two(self):
		val = self.counter
		val += 2
		time.sleep(0.1)
		self.counter = val
		print '***** ',self.counter, threading.current_thread().getName()


my_counter = Counter()

def class_counter_1():
	global my_counter
	for i in range(10):
		my_counter.add_one()

def class_counter_2():
	global my_counter
	for i in range(10):
		my_counter.add_two()



thread1 = threading.Thread(target = class_counter_1)
thread2 = threading.Thread(target = class_counter_2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print my_counter.counter


'''
####  1 Thread-1
*****  3 Thread-2
####  4 Thread-1
*****  6 Thread-2
####  7 Thread-1
*****  9 Thread-2
####  10 Thread-1
*****  12 Thread-2
####  13 Thread-1
*****  15 Thread-2
####  16 Thread-1
*****  18 Thread-2
####  19 Thread-1
*****  21 Thread-2
####  22 Thread-1
*****  24 Thread-2
####  25 Thread-1
*****  27 Thread-2
####  28 Thread-1
*****  30 Thread-2
30
'''




















