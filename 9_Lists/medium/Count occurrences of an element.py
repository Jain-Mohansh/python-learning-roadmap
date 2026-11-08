# Count occurrences of an element
number = [1,1,2,2,1, 2, 3, 4, 5, 6, 7, 8, 2, 9, 10]

for i in set(number):
    print(i, "occurs", number.count(i), "times")