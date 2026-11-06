# Create a function that returns another function

def outer():
    def inner():
        return 'Hello, Welcome!'

    return inner

result = outer()

print(result())