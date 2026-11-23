# Search for a username using for-else

usernames = ["rahul", "amit", "priya", "rohit", "neha"]

search = input("Enter username to search: ")

for name in usernames:
    if name == search:
        print("Username found!")
        break
else:
    print("Username not found!")