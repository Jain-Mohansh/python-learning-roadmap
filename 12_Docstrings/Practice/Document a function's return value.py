# Document a function's return value

def greet_func(name):
    '''Description:
    
    Parameters : 

    [name] type<str>

    Returns : 

    Give the output in the format "hello, <name>"'''
    return(f'hello, {name}')

print(greet_func.__doc__)
print(greet_func('Bingo'))