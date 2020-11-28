@decorator
def apply(func,*args,**kw):
    return func(*args,**kw)

@decorator
class apply:
    def __init__(self,*args,**kw):
        self.args = args
        self.kw = kw

    def __call__(self,func):
        return func(*self.args,**self.kw)

#
#Usage in both cases:
#
@apply
def test():
    return 'test'

assert test == 'test'

@apply(2,3)
def test(a,b):
    return a + b

assert test is 5
