# Create a menu using match-case
menu = '1. Add \n2. Subract \n3. Multiply'
print(menu)
choice = int(input('Enter the chioce : '))

match choice:
    case 1:
        print('You selected Add')
    case 2:
        print('You selected Subtract')
    case 3:
        print('You selected Multiply')