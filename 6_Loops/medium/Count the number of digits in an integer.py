# Count the number of digits in an integer
number = int(input('Enter the number : '))
digits = 0
while number > 0:
    number = (number) // 10 
    digits += 1

print(digits)