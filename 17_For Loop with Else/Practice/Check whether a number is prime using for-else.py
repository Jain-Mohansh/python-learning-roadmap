# Check whether a number is prime using for-else

number = int(input("Enter the number : "))

for i in range(2,number):
    if number % i == 0:
        print("Not a Prime Number")
        break
else:
    print("Prime number")