def synchronized(lock):
    '''Synchronization decorator.'''


    def wrap(f):
        def new_function(*args, **kw):
            lock.acquire()
            try:
                return f(*args,  **kw)
            finally:
                lock.release()
        return new_function
    return wrap

#Example usage:

from threading import Lock
my_lock = Lock()

@synchronized(my_lock)
def critical(*args):
    #Interesting stuff goes here.
    pass

@snchronized(my_lock)
def critical2(*args):
    # Other interesting stuff goes here.
    pass
