class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self,*args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result

#
#sample use
#

>>>@memoize
...def foo(a,b):
...    return a * b
>>>foo(2,4)
8
>>>foo
{(2,4):8}
>>>foo('hi',3)
'hihihi'
>>>foo
{(2,4):8,('hi',3):'hihih'}
