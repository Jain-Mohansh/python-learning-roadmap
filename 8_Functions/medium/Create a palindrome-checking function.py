# Create a palindrome-checking function

def is_palindrome(a):

    if str(a) == str(a)[::-1]:
        return f'{a} is a Palindrome'
    else:
        return f'{a} is not a Palindrome'

print(is_palindrome('moosoom'))