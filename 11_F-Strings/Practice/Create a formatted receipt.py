# Create a formatted receipt

name = input("Enter Customer Name : ")
product = input("Enter Product Name : ")
price = float(input("Enter Product Price : ₹"))
quantity = int(input("Enter Quantity : "))

total = price * quantity


print("\n========= CUSTOMER RECEIPT =========")

print(f"Customer Name : {name}")
print(f"Product Name  : {product}")
print(f"Price         : ₹{price:.2f}")
print(f"Quantity      : {quantity}")
print("-------------------------------------")
print(f"Total Amount  : ₹{total:.2f}")

print("=====================================")
print("          THANK YOU!")