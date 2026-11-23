# Search for an element using for-else

numbers = [10, 20, 30, 40, 50]

search = int(input("Enter an element to search: "))

for num in numbers:
    if num == search:
        print("Element found!")
        break
else:
    print("Element not found!")