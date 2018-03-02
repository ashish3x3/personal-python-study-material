

Python interpreter only used reference counting

Python uses reference counting to keep track of when to get rid of objects
as soon as the last reference to an object goes away, the object is destroyed.

Starting with version 2.0, Python also provides a cyclic garbage collector, which runs at regular intervals. This collector looks for data structures that point to themselves, and does what it can to break the cycles.

You can use the gc.collect function to force full collection. This function returns the number of objects destroyed by the collector.


def make_cycle():
    l = []
    l.append(l)


make_cycle()

Python schedules garbage collection based upon a threshold of object allocations and object deallocations. When the number of allocations minus the number of deallocations are greater than the threshold number, the garbage collector is run. gc.get_threshold()

This is aggravated by the fact that the automatic garbage collection places high weight upon the NUMBER of free objects, not on how large they are. Thus any portion of your code which frees up large blocks of memory is a good candidate for running manual garbage collection.

Although an application should be written to be as free of reference cycles as possible, it is a good idea to have a strategy for how to deal with them. gc.collect()


Prior to Python version 2.0, the Python interpreter only used reference counting for memory management. Reference counting works by counting the number of times an object is referenced by other objects in the system. When references to an object are removed, the reference count for an object is decremented. When the reference count becomes zero the object is deallocated.
Reference counting is extremely efficient but it does have some caveats. One such caveat is that it cannot handle reference cycles. A reference cycle is when there is no way to reach an object but its reference count is still greater than zero. The easiest way to create a reference cycle is to create an object which refers to itself as in the example below:


def make_cycle():
    l = []
    l.append(l)


make_cycle()
Because make_cycle() creates an object l which refers to itself, the object l will not automatically be freed when the function returns. This will cause the memory that l is using to be held onto until the Python garbage collector is invoked.


Automatic Garbage Collection of Cycles
Because reference cycles are take computational work to discover, garbage collection must be a scheduled activity. Python schedules garbage collection based upon a threshold of object allocations and object deallocations. When the number of allocations minus the number of deallocations are greater than the threshold number, the garbage collector is run. One can inspect the threshold for new objects(objects in Python known as generation 0 objects) by loading the gc module and asking for garbage collection thresholds:
import gc
print "Garbage collection thresholds: %r" % gc.get_threshold()
Garbage collection thresholds: (700, 10, 10)
Here we can see that the default threshold on the above system is 700. This means when the number of allocations vs. the number of deallocations is greater than 700 the automatic garbage collector will run.


Automatic garbage collection will not run if your Python device is running out of memory
instead your application will throw exceptions, which must be handled or your application crashes. This is aggravated by the fact that the automatic garbage collection places high weight upon the NUMBER of free objects, not on how large they are. Thus any portion of your code which frees up large blocks of memory is a good candidate for running manual garbage collection.


Recommendations

Do not run garbage collection too freely, as it can take considerable time to evaluate every memory object within a large system. For example, one team having memory issues tried calling gc.collect() between every step of a complex start - up process, increasing the boot time by 20 times (2000 %). Running it more than a few times per day - without specific design reasons - is likely a waste of device resources.
Run manual garbage collection after your application has completed start up and moves into steady - state operation. This frees potentially huge blocks of memory used to open and parse file, to build and modify object lists, and even code modules never to be used again. For example, one application reading XML configuration files was consuming about 1.5MB of temporary memory during the process. Without manual garbage collection, there is no way to predict when that 1.5MB of memory will be returned to the python memory pools for reuse.
Run manual garbage collection after infrequently run sections of code which use and then free large blocks of memory. For example, consider running garbage collection after a once - per - day task which evaluates thousands of data points, creates an XML 'report', and then sends that report to a central office via FTP or SMTP / email. One application doing such daily reports was creating over 800K worth of temporary sorted lists of historical data. Piggy - backing gc.collect() on such daily chores has the nice side - effect of running it once per day for 'free'.
Consider manually running garbage collection either before or after timing - critical sections of code to prevent garbage collection from disturbing the timing. As example, an irrigation application might sit idle for 10 minutes, then evaluate the status of all field devices and make adjustments. Since delays during system adjustment might affect field device battery life, it makes sense to manually run garbage collection as the gateway is entering the idle period AFTER the adjustment process - or run it every sixth or tenth idle period. This insures that garbage collection won't be triggered automatically during the next timing - sensitive period.


First we observe that reference cycles can only be created by container objects. These are objects which can hold references to other objects. In Python lists, dictionaries, instances, classes, and tuples are all examples of container objects. Integers and strings are not containers.


************************* Generational garbage collection ** ******************************

Optimizing garbage collections
https: // www.youtube.com / watch?v = HBd7yVzJllw

newest object usually die quicky.bcz the are created inside the fucntion call, effectolderst object tend to stay longer
GC groups objects into generations

short lived gen - 0
medium gen - 1
long lived gen - 2

when an objetc survives a GC it is promoted to the next generations

GC compacts gen - 0 objects most odten


more the GC runs the bigger the impact on performances


Teh GC will run individually for ech generatiosna dn will ove the survidved obejcts to next highere generations
and GC will run for each genration only iof its threshod of memory is exceeded..


GC runs when:
Gen - 0 objets reach 256K
Gen - 1 object reach 2MB
Gen - 2 objcts reach 10MB
System remory is low


import gc

# create a simple object that links to itself


class Node:

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def addchild(self, node):
        node.parent = self
        self.children.append(node)

    def __repr__(self):
        return "<Node %s at %x>" % (repr(self.name), id(self))


# set up a self-referencing structure
root = Node("monty")

root.addchild(Node("eric"))
root.addchild(Node("john"))
root.addchild(Node("michael"))

# remove our only reference
del root

print gc.collect(), "unreachable objects"
print gc.collect(), "unreachable objects"

12 unreachable objects
0 unreachable objects


# Below is an example with a custom class that has a destructor(del(self), that print out "Object 1 being destructed" or similar. The gc is the garbage collector module, that automatically deletes objects with a reference count of 0. It's there for convenience, as otherwise there is no guarantee when the garbage collector is run.

import gc


class Noisy(object):
    def __init__(self, n):
        self.n = n

    def __del__(self):
        print "Object " + str(self.n) + " being destructed"


class example(object):
    def exampleMethod(self, n):
        aVar = Noisy(n)
        return aVar


a = example()
a.exampleMethod(1)
b = a.exampleMethod(2)
gc.collect()
print "Before b is deleted"
del b
gc.collect()
print "After b is deleted"
The result should be as follows:

Object 1 being destructed
While b lives
Object 2 being destructed
After b is deleted
Notice that the first Noisy object is deleted after the method is returned, as it is not assigned to a variable, so has a reference count of 0, but the second one is deleted only after the variable b is deleted, leaving a reference count of 0.
