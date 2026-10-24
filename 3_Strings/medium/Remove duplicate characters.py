# Remove duplicate characters from a string

a = input('Enter a string: ')
result = ''

for char in a:
    if char not in result:
        result += char
    else:
        print(f'{char} is duplicate')

print(result)
