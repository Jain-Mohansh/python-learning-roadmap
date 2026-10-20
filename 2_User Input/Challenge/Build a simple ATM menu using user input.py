# Build a simple ATM menu using user input
# Build a simple ATM menu using user input

menu = '''1. Check Balance
2. Deposit
3. Withdraw
4. Exit
'''

balance = int(input('Enter the balance amount : '))

print(menu)

choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print(f"Your current balance is: ₹{balance}")

    case 2:
        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Your new balance is: ₹{balance}")
        else:
            print("Invalid deposit amount.")

    case 3:
        amount = int(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount <= balance:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Your remaining balance is: ₹{balance}")
        else:
            print("Insufficient balance.")

    case 4:
        print("Thank you for using the ATM!")

    case _:
        print("Invalid choice. Please select 1-4.")
