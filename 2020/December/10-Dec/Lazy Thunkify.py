import threading, sys, functools, traceback

def lazy_thunkify(f):
    """Make a function immediately return a function of no args which, when called,
    waits for the result, which will start being processed in another thread."""

    @functools.wraps(f)
    def lazy_thunked(*args, **kwargs):
        wait_event = threading.Event()

        result = [None]
        exc = [False, None]

        def worker_func():
            try:
                func_result = f(*args, **kwargs)
                result[0] = func_result
            except Exception, e:
                exc[0] = True
                exc[1] = sys.exc_info()
                print "Lazy thunk has thrown an exception (will be raised on
                thunk()):/n%s"%(
                traceback.format_exc())
                finally:
                    wait_event.set()

            def thunk():
                wait_event.wait()
                if exc[0]:
                    raise exc[1][0], exc[1][1], exc[1][2]

                return result[0]

            threading.Thread(target=worker_func).start()

            return thunk

        return lazy_thunked

#example
@lazy_thunkify
def slow_double(i):
    print "Multiplying...."
    time.sleep(5)
    print "Done multiplying!"
    return i*2


def maybe_multiply(x):
    double_thunk = slow_double(x)
    print "Thinking..."
    time.sleep(3)
    time.sleep(3)
    time.sleep(1)
    if x == 3:
        print "Using it!"
        res = double_thunk()
    else:
        print "Not using it."
        res = None
    return res

#both take 7 seconds
maybe_multiply(10)
maybe_multiply(3)
