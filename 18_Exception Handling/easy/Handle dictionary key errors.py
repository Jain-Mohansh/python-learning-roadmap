# Handle dictionary key errors
my_dict = {"name": "Rahul"}

try:
    print(my_dict["age"])
except KeyError:
    print("Dictionary key error")