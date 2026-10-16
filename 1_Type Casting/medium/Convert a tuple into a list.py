#Convert a tuple into a list

a = 1,2,3,4,'hi'
print(f'{a}\n{type(a)}')
a = list(a)
print(f'{a}\n{type(a)}')