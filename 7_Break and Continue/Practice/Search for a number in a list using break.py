# Search for a number in a list using break
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search = int(input('Enter the number to search in list: '))

for i in l:
    if search == i:
        print(f'{search} element found at index {l.index(search)}')
        break
else:
    print(f'{search} is not in the list')