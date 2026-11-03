# Stop a loop when the user enters quit

while True:
    user_input = input("Enter something (type 'quit' to stop): ")

    if user_input == "quit":
        print("Loop stopped!")
        break

    print("You entered:", user_input)