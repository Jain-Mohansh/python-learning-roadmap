# Handle invalid float input
try:
    num = float(input("Enter a float: "))
except ValueError:
    print("Invalid float input")