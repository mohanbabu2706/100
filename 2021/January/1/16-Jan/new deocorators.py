class Example(object):
    @apply #doesn't exist in python 3
    def myattr():
        doc = '''This is the doc string.'''

        def fget(self):
            return self._half * 2

        def fset(self,value):
            self._half = value / 2

        def fdel(self):
            del self._half

        return property(**locals())
    #myattr = myattr() #works in python 2 and 3
