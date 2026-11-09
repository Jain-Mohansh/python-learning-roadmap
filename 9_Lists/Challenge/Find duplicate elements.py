# Find duplicate elements

# Find duplicate elements
a = [1, 2, 3, 4, 2, 1, 3]

unique = []
duplicates = []

for i in a:
    if i not in unique:
        unique.append(i)
    elif i not in duplicates:
        duplicates.append(i)

print(f'Original List: {a}')
print(f'Duplicate Elements: {duplicates}')
print(f'Without Duplicates: {unique}')