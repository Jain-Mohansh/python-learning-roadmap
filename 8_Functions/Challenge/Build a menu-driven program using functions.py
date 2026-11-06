# Create a menu-driven program using functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 'Cannot divide by zero'
    else:
        return a / b

# Display menu
def menu():
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')

# Menu-driven program
while True:
    menu()

    choice = int(input('Enter your choice : '))

    if choice == 5:
        print('Thank you!')
        break

    a = int(input('Enter first number : '))
    b = int(input('Enter second number : '))

    if choice == 1:
        print('Result :', add(a, b))

    elif choice == 2:
        print('Result :', subtract(a, b))

    elif choice == 3:
        print('Result :', multiply(a, b))

    elif choice == 4:
        print('Result :', divide(a, b))

    else:
        print('Invalid choice')