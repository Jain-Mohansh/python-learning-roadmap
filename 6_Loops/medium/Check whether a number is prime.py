# Check whether a number is prime
number = int(input('Enter the number : '))
reminders = []
if number > 1:
    for i in range(1,number+1):
        check = number % i
        if check == 0:
            reminders.append(check)



if reminders.count(0) == 2:
    print(f"The number {number} is a prime number.")
else:
    print(f"The number {number} is not a prime number.")
