


http://effbot.org/zone/thread-synchronization.htm




Conditions # ###

A condition is a more advanced version of the event object. A condition represents some kind of state change in the application, and a thread can wait for a given condition, or signal that the condition has happened.

 Here’s a simple consumer/producer example. First, you need a condition object:

# represents the addition of an item to a resource
condition = threading.Condition()

The producing thread needs to acquire the condition before it can notify the consumers that a new item is available:

# producer thread
... generate item
condition.acquire()
... add item to resource
condition.notify() # signal that a new item is available
condition.release()
The consumers must acquire the condition (and thus the related lock), and can then attempt to fetch items from the resource:

# consumer thread
condition.acquire()
while True:
    ... get item from resource
    if item:
        break
    condition.wait() # sleep until item becomes available
condition.release()
... process item
The wait method releases the lock, blocks the current thread until another thread calls notify or notifyAll on the same condition, and then reacquires the lock. If multiple threads are waiting, the notify method only wakes up one of the threads, while notifyAll always wakes them all up.

To avoid blocking in wait, you can pass in a timeout value, as a floating-point value in seconds. If given, the method will return after the given time, even if notify hasn’t been called. If you use a timeout, you must inspect the resource to see if something actually happened.

To associate the condition with an existing lock, pass the lock to the Condition constructor. This is also useful if you want to use several conditions for a single resource:

lock = threading.RLock()
condition_1 = threading.Condition(lock)
condition_2 = threading.Condition(lock)


Note that the condition object is associated with a lock, and that lock must be held before you can access the condition. Likewise, the condition lock must be released when you’re done accessing the condition. In production code, you should use try-finally or with, as shown earlier.

lock = threading.Lock()
def get_first_part():
    lock.acquire()
    try:
        ... fetch data for first part from shared object
    finally:
        lock.release()
    return data