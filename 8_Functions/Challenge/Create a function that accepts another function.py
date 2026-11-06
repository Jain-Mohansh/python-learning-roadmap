# Create a function that accepts another function

def greet():
    return 'Hello, Welcome!'

def display(func):
    return func()

print(display(greet))