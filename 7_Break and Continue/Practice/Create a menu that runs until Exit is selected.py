# Create a menu that runs until Exit is selected
menu = '''1. Option 1
2. Option 2
3. Option 3
4. Option 4
4. Exit
'''
while True:
    choice = int(input('Enter the choice (1-5) : '))

    match choice:
        case 1:
            print('You Have selected Option 1')
        case 2:
            print('You Have selected Option 2')
        case 3:
            print('You Have selected Option 3')
        case 4:
            print('You Have selected Option 4')
        case 5:
            print('Exiting Program...')
            break
        case _:
            print('Invalid choice!!, Choose from 1-5')