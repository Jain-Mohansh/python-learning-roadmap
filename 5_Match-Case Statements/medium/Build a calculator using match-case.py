# Build a calculator using match-case
menu = '1. Add \n2. Subract \n3. Multiply \n4. Devision \n5. Exit'
print(menu)
number1 = int(input('Enter the number 1 : '))
number2 = int(input('Enter the number 2 : '))
choice = int(input('Enter the chioce (1-5) : '))

match choice:
    case 1:
        print(number1 + number2)
    case 2:
        print(number1 - number2)
    case 3:
        print(number1 * number2)
    case 4:
        if number2 != 0:
            print(number1 / number2)
        else:
            print("Can't devide by zero.")
    case 5:
        print('Thanks fou using!!')
    case _:
        print('Invalid Choice !!')