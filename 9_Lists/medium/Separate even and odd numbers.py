# Separate even and odd numbers
a = [1,2,3,4,5,6,7,8,9,10]

odd_list = list(filter(lambda x: x%2 != 0, a))
even_list = list(filter(lambda x: x%2 == 0, a))
print(f'Original List : {a}')
print(f'Odd List : {odd_list}')
print(f'Even List : {even_list}')