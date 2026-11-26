# Handle invalid integer input
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Invalid integer input")