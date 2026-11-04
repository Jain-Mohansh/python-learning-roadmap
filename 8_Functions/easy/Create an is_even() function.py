# Create an is_even() function
def is_even(a):
    if a%2 == 0:
        return f'{a} is Even.'
    else:
        return f'{a} is not Even'

print(is_even(8))
print(is_even(9))