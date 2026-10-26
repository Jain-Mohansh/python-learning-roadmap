# Create an age-based ticket pricing system

'''
Age-Based Ticket Pricing:
    Age below 0              → Invalid age
    Age below 5              → Free ticket
    Age 5-12                 → ₹100 ticket
    Age 13-17                → ₹150 ticket
    Age 18-59                → ₹250 ticket
    Age 60 and above         → ₹120 ticket

'''



age = int(input('Enter Your age : '))
if age < 0:
    print('Invalid Age!!')
    price = None
elif age >= 0 and age < 5 :
    price = 0
    print(f'Your Age : {age}')
    print(f'Fare Price : {price}')  
elif age <= 12:
    price = 100
    print(f'Your Age : {age}')
    print(f'Fare Price : {price}')
elif age <= 17:
    price = 150
    print(f'Your Age : {age}')
    print(f'Fare Price : {price}')
elif age < 60:
    price = 250
    print(f'Your Age : {age}')
    print(f'Fare Price : {price}')
elif age >= 60:
    price = 120
    print(f'Your Age : {age}')
    print(f'Fare Price : {price}')

