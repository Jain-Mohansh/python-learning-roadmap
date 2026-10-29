# Build a simple ATM menu
menu = '''
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
'''

print(menu)

balance = 5000

choice = int(input('Enter your choice (1-4): '))

match choice:
    case 1:
        print(f'Your current balance is ₹{balance}')

    case 2:
        deposit = int(input('Enter amount to deposit: '))
        if deposit > 0:
            balance += deposit
            print(f'₹{deposit} deposited successfully!')
            print(f'Your new balance is ₹{balance}')
        else:
            print('Please enter a valid amount.')

    case 3:
        withdraw = int(input('Enter amount to withdraw: '))
        if 0 < withdraw <= balance:
            balance -= withdraw
            print(f'₹{withdraw} withdrawn successfully!')
            print(f'Your remaining balance is ₹{balance}')
        elif withdraw <= 0:
            print('Please enter a valid amount.')
        else:
            print('Insufficient balance!')

    case 4:
        print('Thank you for using Python ATM. Goodbye!')

    case _:
        print('Invalid choice! Please select between 1 and 4.')
