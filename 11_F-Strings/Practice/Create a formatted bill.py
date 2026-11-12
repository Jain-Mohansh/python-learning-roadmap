# Create a formatted bill

name = input("Enter Customer Name : ").capitalize()

products = {
    "Apple": 80,
    "Banana": 45,
    "Mango": 120
}

choice = input("Enter Product (Apple, Banana, Mango) : ").capitalize()

quantity = int(input("Enter Quantity : "))

price = products.get(choice)

total = price * quantity

print("\n========== BILL ==========")

print(f"Customer Name : {name}")
print(f"Product       : {choice}")
print(f"Price         : ₹{price}")
print(f"Quantity      : {quantity}")
print(f"Total Amount  : ₹{total}")

print("==========================")
print("     THANK YOU!")