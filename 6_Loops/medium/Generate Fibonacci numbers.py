# Generate Fibonacci numbers
num = int(input('Enter the number of terms you want : '))
a= 0
b = 1

for i in range(num):
    c = a + b
    a = b
    b = c
    print(c)