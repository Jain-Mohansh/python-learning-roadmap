# Remove duplicates
a = [1,2,3,4,2,1,3]
not_dublicate = []
for i in a:
    if i not in not_dublicate:
        not_dublicate.append(i)

print(f'Original List : {a}')
print(f'Not Duplicate : {not_dublicate}')