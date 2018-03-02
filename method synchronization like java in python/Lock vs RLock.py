


http://effbot.org/zone/thread-synchronization.htm





Lock and RLock(re-entrant locks.)

lock = threading.Lock()
lock.acquire()
lock.acquire() # this will block

lock = threading.RLock()
lock.acquire()
lock.acquire() # this won't block

The RLock class is a version of simple locking that only blocks if the lock is held by another thread. While simple locks will block if the same thread attempts to acquire the same lock twice, a re-entrant lock only blocks if another thread currently holds the lock. If the current thread is trying to acquire a lock that it’s already holding, execution continues as usual.

The second thing to notice is that I'm now using an RLock instead of a normal lock. This is a re-entrant lock and allows a thread to call acquire on a lock more than once if it already holds the lock.

This ensures that if a method calls another method internally it will not cause deadlock as a thread tries to acquire a lock it already owns. In fact we might have wanted to use an RLock for our previous method decorator - otherwise recursion would cause a deadlock.

if U don't define RLock, line 41 will cause deadlock becasue the thread will again try to call lock.acquire() on an already acquired lock. RLock allow U to call lock.acqauire() on an already acquired lock more than once. and the execution won't halt, otherwise it will hault after entering thread number 1. Though line 41 is not required as the function it is calling is already under thread sync

@synchronized_with_lockname('_lock')
	def dosquare(self):
		self.num+=1
		time.sleep(0.1)
		self.num = self.num * self.num

@synchronized_with_lockname('_lock')
	def counter(self):
		for i in range(3):
			print 'Enter *********** ',self.num,threading.current_thread().getName()
			self.dosquare()
			print 'Exit *********** ',self.num,threading.current_thread().getName()

thread1 = threading.Thread(target = ist.counter)
thread2 = threading.Thread(target = ist.counter)


lock = threading.Lock()

def get_first_part():
    lock.acquire()
    try:
        ... fetch data for first part from shared object
    finally:
        lock.release()
    return data

def get_second_part():
    lock.acquire()
    try:
        ... fetch data for second part from shared object
    finally:
        lock.release()
    return data

def get_both_parts():
    first = get_first_part()
    second = get_second_part()
    return first, second

The problem here is that if some other thread modifies the resource between the two calls, we may end up with inconsistent data. The obvious solution to this is to grab the lock in this function as well:

def get_both_parts():
    lock.acquire()
    try:
        first = get_first_part()
        second = get_second_part()
    finally:
        lock.release()
    return first, second
However, this won’t work; the individual access functions will get stuck, because the outer function already holds the lock.

Re-Entrant Locks (RLock) #
The main use for this is nested access to shared resources, as illustrated by the example in the previous section. To fix the access methods in that example, just replace the simple lock with a re-entrant lock, and the nested calls will work just fine.

lock = threading.RLock()

def get_first_part():
    ... see above

def get_second_part():
    ... see above

def get_both_parts():
    ... see above

































