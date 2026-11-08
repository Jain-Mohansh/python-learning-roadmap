# Rotate a list
a = [1,2,3,4,5]

a.insert(0, a[-1])
a.pop()
print(a)