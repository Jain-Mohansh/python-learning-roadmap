# Find the second-largest number
number = [23, 67, 12, 89, 45, 51, 34, 76, 10, 95, 48, 62, 39, 81, 27]
print(number)
number.sort()
print(number)

second_largest = number[-2]
print(f'Second Largest : {second_largest}')