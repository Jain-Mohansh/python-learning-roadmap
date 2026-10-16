#Convert a list of numeric strings into a list of integers

a = ['1','2','3','4']
b = []
print(f'{a}\n{type(a)}')
for i in a:
    i = int(i)
    b.append(i)

print(f'{b}\n{type(b)}')
    