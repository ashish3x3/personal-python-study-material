

# http://theorangeduck.com/page/synchronized-python
# http://caffeinatedideas.com/2014/12/12/java-synchronized-in-python.html


Synchronized in Python


Java gives us some nice threading primitives built into the language including the abstraction of the synchronized keyword. What this keyword ensures is that no two threads will enter the same block marked as synchronized. We can actually build into python almost identical functionality using decorators and some basic meta-programming.

First we'll tackle the synchronized block syntax in Java. It looks like this:

/* Enter critical section */
synchronized(mLock) {
    /* Do critical work */
}
/* Exit critical section */

This can appear pretty much anywhere in Java code and any non-native Object can be used as a lock. For the same in python we don't have to add anything - it actually has this already built in - but instead of the synchronizedwith keyword.

# Enter critical section
with self.lock:
    # Do critical work
# Exit critical section

Pretty straight forward - and the lovely thing about the pythonic way is that the functionality of the "with" keyword can be defined for any class using the __enter__ and __exit__ methods. You might have already seen it being used for files and a host of other things.

There is also a second advantage to using the with keyword over simply wrapping the critical section in self.lock.acquire() and self.lock.release(). Using with ensures that the lock is always released, even if an exception occurs within the critical section. It will ensure that __exit__ is always called, much like the finally statement in a try block.

The second way in which synchronized appears in Java is in a method declaration. It looks something like this.
public class Counter {

    int mTotal;

    public Counter() {
 	mTotal = 0;
    }

    public synchronized void addOne() {
        int val = mTotal;
        val++;
        mTotal = val;
    }
}

This ensures that no two threads can both be inside a class instance' method at the same time. For this example it ensures that the total always get updated correctly.

For Python let us start with something a little simpler than a method. We can build this syntax for plain old functions using our own hand made decorators. The decorator looks something like this:



import threading

def synchronized(func):

    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func



    As you can see, it takes a function, attaches a lock to that function, and wraps the function within that lock. As in Java this ensures that no two threads can be inside the function at the same time. Here is an example of it at work.



    import time

    total = 0

    @synchronized
    def count():
        global total
        curr = total + 1
        time.sleep(0.1)
        total = curr

    def counter():
        for i in range(0,10): count()

    thread1 = threading.Thread(target = counter)
    thread2 = threading.Thread(target = counter)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print total



    With the function count synchronized this script should correctly print out 20 for the value of total. If the decorator is removed then technically the value of total is some unknown between 10 and 20, but in this script it will tend to be 10 as the timing almost always ensures both threads enter the critical section at the same time and the total is updated incorrectly.

    But unfortunately the decorator above wont work for methods. The reason for this is the way in which classes are instanced. If you were to apply the above to a class method it would create a lock across all instances of that method (the actual method function only exists in one place). If we want a lock on a per-instance basis we have to do something else.


    def synchronized_method(method):

        outer_lock = threading.Lock()
        lock_name = "__"+method.__name__+"_lock"+"__"

        def sync_method(self, *args, **kws):
            with outer_lock:
                if not hasattr(self, lock_name): setattr(self, lock_name, threading.Lock())
                lock = getattr(self, lock_name)
                with lock:
                    return method(self, *args, **kws)

        return sync_method

    class Counter:

        def __init__(self):
            self.total = 0

        @synchronized_method
        def add_one(self):
            val = self.total
            val += 1
            self.total = val


    This is a bit more messy but we can solve it by taking advantage of the fact that all method functions take a self value as their first parameter representing the class instance. ..

    This new decorator basically checks if the class instance already has a lock for the method to use. If a lock exists it uses it, otherwise it creates a new one and attaches it to the instance.

    Worth nothing that as this class instance lock is created at run-time we need an outer lock, created before anything in the instance, to ensure there is no race condition with who gets to create the first class instance lock (imagine two threads calling this method for the first time, at the same time).

    For this we create an outer lock at the time of class definition (when the decorator is applied) and use this to ensure only one instance lock is created.

    In Java method synchronization all synchronization methods refer to the same object instance lock. In our python example above it is slightly different. Each of our methods uses a different lock.

    We can create something more similar though. What we can do is to lock whenever we wish to manipulate a certain member of a class instance.


    import threading
    import time

    def synchronized_with_attr(lock_name):

        def decorator(method):

            def synced_method(self, *args, **kws):
                lock = getattr(self, lock_name)
                with lock:
                    return method(self, *args, **kws)

            return synced_method

        return decorator


    class Counter:

        def __init__(self):
            self.lock = threading.RLock()
            self.total = 0

        @synchronized_with_attr("lock")
        def add_one(self):
            val = self.total
            val += 1
            time.sleep(0.1)
            self.total = val

        @synchronized_with_attr("lock")
        def add_two(self):
            val = self.total
            val += 2
            time.sleep(0.1)
            self.total = val


            The most obvious difference is that we are now passing in the decorator a string with the name of the lock attribute. The reason for this is that decorators are applied at the time the class is defined, not at the point at which it is instanced. Before it is instanced python has no idea that self.lock actually exists. Because of this we have to give the name as a string and rely on the fact that it will accurately find the correct member once the class is instanced.

            The second thing to notice is that I'm now using an RLock instead of a normal lock. This is a re-entrant lock and allows a thread to call acquire on a lock more than once if it already holds the lock. This ensures that if a method calls another method internally it will not cause deadlock as a thread tries to acquire a lock it already owns. In fact we might have wanted to use an RLock for our previous method decorator - otherwise recursion would cause a deadlock.

            Finally if we take a look at our decorator synchronized_with_attr we realize this isn't a decorator in itself, but in fact a function which returns a decorator. This is a key aspect of how we argument decorators and begins to show their full power.

            Sometimes we wish to lock over all of the methods for a class. Creating what is essentially a thread safe data structure. In Java this is easy - we just add the synchronized keyword to the class definition.



            public synchronized class Counter {

                int mTotal;

                public MyClass() {
                    mTotal = 0;
                }

                public void addOne() {
                    int val = mTotal;
                    val += 1;
                    mTotal = val;
                }

                public void addTwo() {
                    int val = mTotal;
                    val += 2;
                    mTotal = val;
                }
            }


            We can do this in python too, though the solution becomes a bit more complicated. Let us try and create an appropriate decorator for a class.



            import threading
            import types

            def synchronized_with(lock):

                def decorator(func):

                    def synced_func(*args, **kws):
                        with lock:
            	        return func(*args, **kws)
                    return synced_func

                return decorator


            def synchronized_class(sync_class):

                lock = threading.RLock()

                orig_init = sync_class.__init__
                def __init__(self, *args, **kws):
                    self.__lock__ = lock
                    orig_init(self, *args, **kws)
                sync_class.__init__ = __init__

                for key in sync_class.__dict__:
                    val = sync_class.__dict__[key]
                    if type(val) is types.FunctionType:
                        decorator = synchronized_with(lock)
                        sync_class.__dict__[key] = decorator(val)

                return sync_class


                Let me explain what is happening here.

                The first thing that happens is we create a new lock for the class to use. We then override the __init__ method of the class so that it first assigns this new lock as the class member __lock__ before calling the old __init__ function. We then loop over all of the items in the class dictionary. We check for which ones are functions, and if they are we apply our synchronized_with decorator to them with the lock we created at the beginning. We then return the modified class. And that's it! We have a synchronized class.

                There is one more nice tweak we can do, which is to combine all of these new decorators into one function that decides which decorator is appropriate to apply. This is fairly straight forward - we simply look at the argument to the function. If the argument is a lock then we know we must return a new decorator using that lock. If the argument is a string we try to apply the attribute synchronization. If we get anything else (such as a function or a class) then we apply the decorator as usual.



                import thread
                import threading
                import types

                def synchronized_with_attr(lock_name):

                    def decorator(method):

                        def synced_method(self, *args, **kws):
                            lock = getattr(self, lock_name)
                            with lock:
                                return method(self, *args, **kws)

                        return synced_method

                    return decorator


                def syncronized_with(lock):

                    def synchronized_obj(obj):

                        if type(obj) is types.FunctionType:

                            obj.__lock__ = lock

                            def func(*args, **kws):
                                with lock:
                                    obj(*args, **kws)
                            return func

                        elif type(obj) is types.ClassType:

                            orig_init = obj.__init__
                            def __init__(self, *args, **kws):
                                self.__lock__ = lock
                                orig_init(self, *args, **kws)
                            obj.__init__ = __init__

                            for key in obj.__dict__:
                                val = obj.__dict__[key]
                                if type(val) is types.FunctionType:
                                    decorator = syncronized_with(lock)
                                    obj.__dict__[key] = decorator(val)

                            return obj

                    return synchronized_obj


                def synchronized(item):

                    if type(item) is types.StringType:
                        decorator = synchronized_with_attr(item)
                        return decorator(item)

                    if type(item) is thread.LockType:
                        decorator = syncronized_with(item)
                        return decorator(item)

                    else:
                        new_lock = threading.Lock()
                        decorator = syncronized_with(new_lock)
                        return decorator(item)


                And with about 50 lines of code we've added the synchronization primitives to python, beautiful!



                @synchronized
                class Counter:

                    def __init__(self):
                        self.counter = 0

                    def add_one(self):
                        val = self.counter
                        val += 1
                        time.sleep(0.1)
                        self.counter = val

                    def add_two(self):
                        val = self.counter
                        val += 2
                        time.sleep(0.1)
                        self.counter = val


                my_counter = Counter()

                def class_counter1():
                    global my_counter
                    for i in range(0,10): my_counter.add_one()

                def class_counter2():
                    global my_counter
                    for i in range(0,10): my_counter.add_two()

                thread1 = threading.Thread(target = class_counter1)
                thread2 = threading.Thread(target = class_counter2)

                thread1.start()
                thread2.start()

                thread1.join()
                thread2.join()

                print my_counter.counter



************************

When you add the synchronized keyword in a method signature or a synchronized block, Java adds the code to acquire the lock on the object currently bound to this.


The end result is that the developer can ensure a method is thread safe simply by stating:

public class LinkedList {
    public synchronized void insert(final Object data) {
        // ...
    }
}

To replicate this behavior in python, we'd need two extra pieces of functionality.

Python objects do not implicitly contain a mutex lock, so we need to allocatean instance of threading.Lock on self during object construction.
We need to acquire this implicit Lock when the method starts and then releasethe Lock whenever flow exits our methods.

The equivalent python code would be:

class LinkedList:
   def__init__(self):
      self._lock = threading.Lock()

   def insert(self):
      with self._lock:
         # ...
         pass

         Decorators
         My first thought was to define a decorator, called synchronized that would return a new method with the locking semantics. Injecting the lock would need to be done in the wrapping method since self isn't defined when the decorator is executed. Here's my first attempt:

         from threading import Lock

         def synchronized(method):
             """
             A decorator object that can be used to declare that execution of a particular
             method should be done synchronous. This works by maintaining a lock object on
             the object instance, constructed for you if you don't have one already, and
             then acquires the lock before allowing the method to execute. This provides
             similar semantics to Java's synchronized keyword on methods.
             """
             def new_synchronized_method(self, *args, **kwargs):
                 if not hasattr(self, "_auto_lock"):
                     self._auto_lock = Lock()
                 with self._auto_lock:
                     return method(self, *args, **kwargs)
             return new_synchronized_method


         class LinkedList:
             @synchronized
             def insert(self, data):
                 pass
         A nice first attempt but horribly broken - the hasattr() check on self and the construction of the Lock object is not thread safe. Solving this problem is simple enough if we can either ensure that _auto_lock is created in the class __init__ method or we introduce a new Lock somewhere else in the process.

         Solving the problem in __init__ can take multiple forms. The simplest solution is just require the user of the synchronized decorator to declare a member called _auto_lock and raise an exception if the lock is missing. Then our decorator would look like:

         from threading import Lock

         def synchronized(method):
             """
             A decorator object that can be used to declare that execution of a particular
             method should be done synchronous. This works by maintaining a lock object on
             the object instance, constructed for you if you don't have one already, and
             then acquires the lock before allowing the method to execute. This provides
             similar semantics to Java's synchronized keyword on methods.
             """
             def new_synchronized_method(self, *args, **kwargs):
                 if hasattr(self, "_auto_lock"):
                     with self._auto_lock:
                         return method(self, *args, **kwargs)
                 else:
                     raise AttributeError("Object is missing _auto_lock")
             return new_synchronized_method

         class LinkedList:
             def __init__(self):
                 # other init logic
                 self._auto_lock = Lock()

             @synchronized
             def insert(self, data):
                 pass
         The downside here is that users are required to make two changes to their classes in order to use the synchronized behavior. This also means that the developer has read the documentation where we mention that they need to add _auto_lock to the self instance. Relying on the user of our decorator is not as automatic as the Java synchronized block.

         The other solution is to introduce a Lock to prevent assigning _auto_lock multiple times. The downside with this approach is the performance hit we need to take when the synchronized method is called the first time on new object instances. To try to make this process somewhat tolerable, we use the check-lock-check pattern, where most long lived objects should skip the lock step for most cases. The code now looks like:

         from threading import Lock

         synchronized_lock = Lock()
         def synchronized(method):
             """
             A decorator object that can be used to declare that execution of a particular
             method should be done synchronous. This works by maintaining a lock object on
             the object instance, constructed for you if you don't have one already, and
             then acquires the lock before allowing the method to execute. This provides
             similar semantics to Java's synchronized keyword on methods.
             """
             def new_synchronized_method(self, *args, **kwargs):
                 if not hasattr(self, "_auto_lock"):
                     with synchronized_lock:
                         if not hasattr(self, "_auto_lock"):
                             self._auto_lock = Lock()
                 with self._auto_lock:
                     return method(self, *args, **kwargs)
             return new_synchronized_method

         class LinkedList:
             @synchronized
             def insert(self, data):
                 pass
         We're now back to only a single change and we modify self in a thread safe fashion. The downside is that we have this glaring performance bottleneck, the global instance of synchronized_lock, across all sections of code that depend on synchronized. I'm also leery of this solution because it does introduce risk of deadlocking in odd ways.

         What we really need is more control over the class as the class is being defined and hooks into the instance creation process.

         Metaclasses
         Python provides the metaclass mechanics if you need more control over the creation of classes or want to perform a bit more "magic" in your code. There are plenty of resources that explain metaclasses in python far better that I could and I would suggest taking a look at them before continuing.

         The first order of business is to create _auto_lock automatically on self. The only action that our user needs to take is to declare that their class definition uses our metaclass. Here's our metaclass solution:

         from threading import Lock

         def wrap_init_with_lock(orig_init):
             """
             A decorator function that will wrap a class __init__ method and adds
             an property called _auto_lock after running the original __init__
             method.
             """
             def new_wrapped_init(self, *args, **kwargs):
                 orig_init(self, *args, **kwargs)
                 self._auto_lock = Lock()
             return new_wrapped_init

         class Synchronized(type):
             """
             This is our metaclass. It needs to be mixed in to objects that want
             to have the Java synchronized semantics.
             """
             def __init__(cls, names, bases, namespace):
                 cls.__init__ = wrap_init_with_lock(cls.__init__)
         Now let's use the new metaclass with the same LinkedList example:

         class LinkedList:
             __metaclass__ = Synchronized

             def insert(self, data):
                 # ...
                 pass
         The first thing to notice is that the metaclass __init__ method doesn't get passed a reference to self (instance of Synchronized) but instead is passed an instance of the object that is mixing in the behaviors of Synchronized (instance of LinkedList). Also interesting is that since our code is being called as part of the object instance creation process, we're in a thread-safe block of code.

         Now we want to provide a synchronized version of our methods. Since we want to make usage of the behavior as simple as possible, we need a new way to determine if a method should be synchronized. We'll do this by naming convention - if the method name starts with synchronized_ then we'll wrap execution of the method to use _auto_lock. Using the cls reference, we can use dir to find the methods with the matching names and then monkey patch them with a decorator-like function.

         from threading import Lock

         def wrap_init_with_lock(orig_init):
             """
             A decorator function that will wrap a class __init__ method and adds
             an property called _auto_lock after running the original __init__
             method.
             """
             def new_wrapped_init(self, *args, **kwargs):
                 orig_init(self, *args, **kwargs)
                 self._auto_lock = Lock()
             return new_wrapped_init

         def wrap_method_with_sync(method):
             """
             A decorator function that wraps any class method with auto locking
             behavior. Before using, you need to ensure that the object reference
             has a _auto_lock property bound to an instance of threading.Lock.
             """
             def new_synchronized_method(self, *args, **kwargs):
                 with self._auto_lock:
                     return method(self, *args, **kwargs)
             return new_synchronized_method

         class Synchronized(type):
             """
             This is our metaclass. It needs to be mixed in to objects that want
             to have the Java synchronized semantics.
             """
             def __init__(cls, names, bases, namespace):
                 cls.__init__ = wrap_init_with_lock(cls.__init__)
                 for methodname in dir(cls):
                     if methodname.startswith("synchronized_"):
                         orig_method = getattr(self, methodname)
                         setattr(self, methodname, wrap_method_with_sync(orig_method))
         With the LinkedList example again:

         class LinkedList:
             __metaclass__ = Synchronized

             def synchronized_insert(self, data):
                 # ...
                 pass
         Now we have Java-like synchronized semantics based purely on the name of the method. It also forces us to declare the synchronized functionality in the method name, serving as good documentation for our code base. The metaclass is also a separate block of code that can be unit tested and reused across the entire system.

         What's The Point?
         The usefulness of these solutions is in the process of trying to bend and morph python into a new and interesting shape through the various extension mechanisms that are provided to us. Decorators are easier to understand but lack all of the extension points for a problem as complex as our synchronized structure. Metaprogramming requires thinking about the problem on a different plane, is difficult to wrap our mind around but also provides us with a lot of ways we can change classes after the code has been written. As a kata, the Java synchronized keyword has proven to be a nice sized problem.




















