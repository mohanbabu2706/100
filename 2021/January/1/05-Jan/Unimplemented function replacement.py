#Annotation wrapper annotation method
def unimplemented(defaultval):
    if(type(defaultval) == type(unimplemented)):
        return lambda: None
    else:
        #Actual annotation
        def unimp_wrapper(func):
            #what we replace the function with
            def wrapper(*arg):
                return defaultval
            return wrapper
        return unimp_wrapper
