# Find intersection of three lists
a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 6]
c = [3, 4, 7]
intersection = []

for i in a:
    if i in b and i in c:
        intersection.append(i)
print(a)
print(b)
print(c)
print(intersection)