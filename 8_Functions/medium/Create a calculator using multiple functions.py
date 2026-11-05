# Create a calculator using multiple functions
def add():
    a = int(input('Enter the number 1 : '))
    b = int(input('Enter the number 2 : '))
    return a + b

def subtract():
    a = int(input('Enter the number 1 : '))
    b = int(input('Enter the number 2 : '))
    return a - b

def devide():
    a = int(input('Enter the number 1 : '))
    b = int(input('Enter the number 2 : '))
    if b!=0:
        return a/b
    else:
        return "can't devide by zero"

def multiply():
    a = int(input('Enter the number 1 : '))
    b = int(input('Enter the number 2 : '))
    return a * b

def exponent():
    a = int(input('Enter the number 1 : '))
    b = int(input('Enter the number 2 : '))
    return a**b

def root():    
    a = int(input('Enter the number 1 : '))
    return a**.5

def calculator():
    menu = '''1. Addition(a,b format)
2. Subtraction(a,b format)
3. Multiplication(a,b format)
4. Devide(a,b format)
5. Exponent(a,b format)
6. Root
    '''
    print(menu)
    choice = int(input("Enter the choice(1-6): "))

    match choice:
        case 1:
           print(add())
        case 2:
            print(subtract())
        case 3:
            print(multiply())
        case 4:
            print(devide())
        case 5:
            print(exponent())
        case 6:
            print(root())
        case _:
            print('Invalid Choice!')

calculator()