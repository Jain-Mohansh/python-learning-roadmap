# Reverse a string recursively

def reverse_string(a):

    if len(a) == 0:
        return a

    return reverse_string(a[1:]) + a[0]

print(reverse_string('Python'))