# Find perfect numbers in a range

for number in range(1,100):
    p = 0
    for i in range(1,number):
        if number%i == 0:
            p += i
    if p == number:
        print(p)
            