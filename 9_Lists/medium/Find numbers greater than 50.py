# Find numbers greater than 50
numbers = [23, 67, 12, 89, 45, 51, 34, 76, 10, 95, 48, 62, 39, 81, 27]

number = list(filter(lambda x: x > 50, numbers))
print(number)