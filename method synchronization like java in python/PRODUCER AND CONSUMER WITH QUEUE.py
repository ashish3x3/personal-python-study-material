

# https://agiliq.com/blog/2013/10/producer-consumer-problem-in-python/

from threading import Thread, Condition
import time
import random

queue = []
MAX_NUM = 10
condition = Condition()

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print "Queue full, producer is waiting"
                condition.wait()
                print "Space in queue, Consumer notified the producer"
            num = random.choice(nums)
            queue.append(num)
            print "Produced", num
            condition.notify()
            condition.release()
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print "Nothing in queue, consumer is waiting"
                condition.wait()
                print "Producer added something to queue and notified the consumer"
            num = queue.pop(0)
            print "Consumed", num
            condition.notify()
            condition.release()
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()
Sample output:

Produced 0
Consumed 0
Produced 0
Produced 4
Consumed 0
Consumed 4
Nothing in queue, consumer is waiting
Produced 4
Producer added something to queue and notified the consumer
Consumed 4
Produced 3
Produced 2
Consumed 3

'''
Explanation:
For consumer, we check if the queue is empty before consuming.
If yes then call wait() on condition instance.
wait() blocks the consumer and also releases the lock associated with the condition. This lock was held by consumer, so basically consumer loses hold of the lock.
Now unless consumer is notified, it will not run.
Producer can acquire the lock because lock was released by consumer.
Producer puts data in queue and calls notify() on the condition instance.
Once notify() call is made on condition, consumer wakes up. But waking up doesn't mean it starts executing.
notify() does not release the lock. Even after notify(), lock is still held by producer.
Producer explicitly releases the lock by using condition.release().
And consumer starts running again. Now it will find data in queue and no IndexError will be raised.

Adding a max size on the queue
Producer should not put data in the queue if the queue is full.

It can be accomplished in the following way:

Before putting data in queue, producer should check if the queue is full.
If not, producer can continue as usual.
If the queue is full, producer must wait. So call wait() on condition instance to accomplish this.
This gives a chance to consumer to run. Consumer will consume data from queue which will create space in queue.
And then consumer should notify the producer.
Once consumer releases the lock, producer can acquire the lock and can add data to queue.

'''



'''
Many people on the internet suggested that I use Queue.Queue instead of using a list with conditions and lock. I agree, but I wanted to show how Conditions, wait() and notify() work so I took this approach.

Let's update our code to use Queue.

Queue encapsulates the behaviour of Condition, wait(), notify(), acquire() etc.
'''


from threading import Thread
import time
import random
from Queue import Queue

queue = Queue(10)

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print "Produced", num
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print "Consumed", num
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()







# http://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Producer_Consumer_using_Queue.php





import threading
import time
import logging
import random
import Queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

BUF_SIZE = 10
q = Queue.Queue(BUF_SIZE)

class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread,self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            if not q.full():
                item = random.randint(1,10)
                q.put(item)
                logging.debug('Putting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random.random())
        return

class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread,self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            if not q.empty():
                item = q.get()
                logging.debug('Getting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random.random())
        return

if __name__ == '__main__':

    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)


    (producer ) Putting 2 : 1 items in queue
    (producer ) Putting 10 : 2 items in queue
    (producer ) Putting 6 : 3 items in queue
    (producer ) Putting 7 : 4 items in queue
    (producer ) Putting 1 : 5 items in queue
    (consumer ) Getting 2 : 4 items in queue
    (consumer ) Getting 10 : 3 items in queue
    (producer ) Putting 1 : 4 items in queue
    (producer ) Putting 8 : 5 items in queue
    (consumer ) Getting 6 : 4 items in queue
    (producer ) Putting 10 : 5 items in queue
    ...

'''
    Since the Queue has a Condition and that condition has its Lock we don't need to bother about Condition and Lock.
    Producer uses Queue.put(item[, block[, timeout]]) to insert data in the queue. It has the logic to acquire the lock before inserting data in queue. If optional args block is true and timeout is None (the default), block if necessary until a free slot is available. If timeout is a positive number, it blocks at most timeout seconds and raises the Full exception if no free slot was available within that time. Otherwise (block is false), put an item on the queue if a free slot is immediately available, else raise the Full exception (timeout is ignored in that case).

    Also put() checks whether the queue is full, then it calls wait() internally and so producer starts waiting.
    Consumer uses Queue.get([block[, timeout]]), and it acquires the lock before removing data from queue. If the queue is empty, it puts consumer in waiting state.
    Queue.get() and Queue.get() has notify() method.

'''