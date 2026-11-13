# View your docstring using help()

class Greet:
    '''This is a greeting class'''
    def greet(self, name):
        '''Takes the name and greet you in the format hello, <name>'''
        return f"hello, {name}"

obj = Greet()
print(obj.greet('Bingo'))
help(Greet)
help(Greet.greet)