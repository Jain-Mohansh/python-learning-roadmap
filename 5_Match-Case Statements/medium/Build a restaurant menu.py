# Build a restaurant menu


# Build a restaurant menu

menu = '''
1. Pizza — ₹150
2. Burger — ₹100
3. Pasta — ₹120
4. Coffee — ₹50
5. Exit'''

print(menu)

choice = int(input('Enter your choice (1-5): '))

match choice:
    case 1:
        print('You selected Pizza. Price: ₹150')
    case 2:
        print('You selected Burger. Price: ₹100')
    case 3:
        print('You selected Pasta. Price: ₹120')
    case 4:
        print('You selected Coffee. Price: ₹50')
    case 5:
        print('Thank you for visiting! Goodbye.')
    case _:
        print('Invalid choice! Please select between 1 and 5.')
