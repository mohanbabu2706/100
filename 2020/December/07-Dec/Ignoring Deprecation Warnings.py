import warnings

def ignore_deprecation_warnings(func):
    '''This is a decorator which can be used to ignore deprecatin warnings
    occuring in a function.'''
    def new_func(*args, **kwargs):
        with warnings.catch_warnings():
            warnings.filtewarnings("ignore", category=DeprecationWarning)
            return func(*args, **kwargs)
    new_func.__name__=func.__name__
    new_func.__doc__=func.__doc__
    new_func.__dict__.update(func.__dict__)
    return new_func

#examples of use

@ignore_deprecation_warnings
def some_function_raising_deprecation_warning():
    warnings.warn("This is a deprecationg warning.",
                  category=DeprecationWarning)

class SomeClass:
    @ignore_deprecation_warnings
    def some_method_raising_deprecation_warning():
        warnings.warn("This is a deprecationg warning.",
                      category=DeprecationWarning)
