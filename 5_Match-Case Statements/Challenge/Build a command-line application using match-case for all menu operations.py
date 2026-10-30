
# Build a command-line ATM application using match-case

balance = 5000

while True:
    print("""
===== Welcome to Python ATM =====

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
""")

    try:
        choice = int(input("Enter your choice (1-4): "))

        match choice:
            case 1:
                print(f"Your current balance is: ₹{balance}")

            case 2:
                amount = float(input("Enter deposit amount: ₹"))

                if amount > 0:
                    balance += amount
                    print(f"₹{amount:.2f} deposited successfully!")
                    print(f"Updated balance: ₹{balance:.2f}")
                else:
                    print("Please enter an amount greater than zero.")

            case 3:
                amount = float(input("Enter withdrawal amount: ₹"))

                if amount <= 0:
                    print("Please enter an amount greater than zero.")
                elif amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= amount
                    print(f"Please collect your cash: ₹{amount:.2f}")
                    print(f"Remaining balance: ₹{balance:.2f}")

            case 4:
                print("Thank you for using Python ATM. Goodbye!")
                break

            case _:
                print("Invalid choice! Please select between 1 and 4.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
