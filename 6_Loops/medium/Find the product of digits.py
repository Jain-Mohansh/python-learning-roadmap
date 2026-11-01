# Find the product of digits

num = input('Enter the number to find the sum of digit : ')
product = 1
for i in num:
    product *= int(i)
print(product)
