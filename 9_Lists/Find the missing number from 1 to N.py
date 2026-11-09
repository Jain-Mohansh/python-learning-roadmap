# Find the missing number from 1 to N
number = [1,3,4,5,6,7,9,10, 13]
number.sort()
# print(number)
missing = []
for i in range(1,max(number)):
    if i not in number:
        missing.append(i)

print(f'Original List : {number}')
print(f'Missing Number : {missing}')
        