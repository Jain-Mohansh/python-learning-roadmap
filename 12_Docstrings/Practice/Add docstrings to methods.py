# Add docstrings to methods

class Class:

    def func(self):
        '''This is a docstring in a method'''
        pass


obj = Class()

print(obj.func.__doc__)