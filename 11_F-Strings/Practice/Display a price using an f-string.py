# Display a price using an f-string

products = {"Apple" : 80,
            "Banana" : 45,
            "Mango" : 120}

choice = input("Enter the choice(Apple, Banana, Mango) : ").capitalize()

print(f"The print of {choice} : ₹{products.get(choice)}")