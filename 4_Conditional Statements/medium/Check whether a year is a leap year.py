# Check whether a year is a leap year
year = int(input('Enter the year to check(Leap or not) : '))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
    