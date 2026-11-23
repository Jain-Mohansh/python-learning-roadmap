# Find whether a number exists in a list

numbers = [1,2,3,4,5,6,7,8,9,12,13,15,75]

number = int(input("Enter the number to check : "))

for i in range(len(numbers)):
    if number == numbers[i]:
        print(f"Number found at index {i}")
        break
else:
    print(f"Number not in list.")