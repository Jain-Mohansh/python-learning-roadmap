# Build a menu-driven calculator

menu = '''1. Addition(a+b)
2. Subtraction(a-b)
3. Multiplication(a*b)
4. Division(a/b)
5. Exit
'''

print(menu)

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))

choice = int(input('Enter the choice (1-5): '))

match choice:
    case 1:
        print(f'The sum of {num1} and {num2} is {num1 + num2}')
    case 2:
        print(f'The subtraction of {num1} and {num2} is {num1 - num2}')
    case 3:
        print(f'The multiplication of {num1} and {num2} is {num1 * num2}')
    case 4:
        if num2 != 0:
            print(f'The division of {num1} and {num2} is {num1 / num2}')
        else:
            print('Cannot divide by zero.')
    case 5:
        print('Exiting calculator...')
    case _:
        print('Invalid choice. Please enter a number between 1 and 5.')