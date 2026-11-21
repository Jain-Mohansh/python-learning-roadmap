# Create a phone book

phone_book = {}

phone_book["Rahul"] = "9876543210"
phone_book["Priya"] = "8765432109"
phone_book["Amit"] = "7654321098"

print("Phone Book:", phone_book)

name = input("Enter name: ")

if name in phone_book:
    print("Phone Number:", phone_book[name])
else:
    print("Contact Not Found")

phone_book["Rahul"] = "9999999999"

phone_book.pop("Amit")

print("Updated Phone Book:", phone_book)