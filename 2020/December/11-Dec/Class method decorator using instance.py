from functools import wraps

def decorate(f):
    '''
    Class method decorator specific to the instance.

    It uses a descriptor to delay the definition of the
    method wrapper.
    '''
    class descript(object):
        def __init__(self, f):
            self.f = f

            def __get__(self, instance, klass):
                if instance is None:
                    #Class method was requested
                    return self.make_unbound(klass)
                return self.make_bound(instance)

            def make_unbound(self, klass):
                @wraps(self.f)
                def wrapper(*args, **kwargs):
                    '''This documentation will vanish :)'''
                    raise TypeError(
                        'unbound method {} () must be called with {} instance '
                        'as first argument (got nothing instead)'.format(
                            self.f.__name__,
                            klass.__name__)
                        )
                return wrapper

            def make_bound(self, instance):
                @wraps(self.f)
                def wrapper(*args, **kwargs):
                    '''This documentation will disapear :)'''
                    print "called the decorated method {} od {}".format(self.f.__name__,instance)

                    return self.f(instance, *args, **kwargs)
                   #this instance does not need the descriptor anymore,
                #let it find the wrapper directly next time:
                setattr(instance, self.f.__name__, wrapper)
                return wrapper

            return descript(f)
