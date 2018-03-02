http://effbot.org/zone/thread-synchronization.htm


Semaphores #
A semaphore is a more advanced lock mechanism. A semaphore has an internal counter rather than a lock flag, and it only blocks if more than a given number of threads have attempted to hold the semaphore. Depending on how the semaphore is initialized, this allows multiple threads to access the same code section simultaneously.

semaphore = threading.BoundedSemaphore()
semaphore.acquire() # decrements the counter
... access the shared resource
semaphore.release() # increments the counter

If the counter reaches zero when acquired, the acquiring thread will block. When the semaphore is incremented again, one of the blocking threads (if any) will run.
Semaphores are typically used to limit access to resource with limited capacity, such as a network connection or a database server.

max_connections = 10
semaphore = threading.BoundedSemaphore(max_connections)