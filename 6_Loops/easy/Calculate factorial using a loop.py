# Calculate factorial using a loop

num = int(input('Enter the number to find the factorial : '))
factorial = 1
for i in range(num, 1, -1):
    factorial *= i
print(factorial)