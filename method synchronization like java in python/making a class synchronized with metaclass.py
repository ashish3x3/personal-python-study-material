import threading

#  http://caffeinatedideas.com/2014/12/12/java-synchronized-in-python.html
def add_lock_to_init(orig_init):

	def wrap_init_with_lock(self, *args, **kwargs):
		orig_init(self, *args, **kwargs)
		orig_init._lock = threading.RLock()
	return wrap_init_with_lock

def wrap_method_with_sync(func):

	def new_wrap_method(self, *args, **kwargs ):
		with self._lock:
			return func(self, *args, **kwargs)
		return new_wrap_method



class Synchronized(type):

	def __init__(cls, names,bases,namespace):
		cls.__init__ = add_lock_to_init(cls.__init__)

		for methodname in dir(cls):
			if methodname.startswith('synchronized__'):
				orig_method = getattr(self, methodname, wrap_method_with_sync(methodname))



class LinkedList:
	__metaclass__ = Synchronized

	def synchronized_insert(self,data):
		print 'sync insert'