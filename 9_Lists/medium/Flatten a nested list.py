# Flatten a nested list
a = [[1, 2], [3, 4]]

result = []

for sublist in a:
    for item in sublist:
        result.append(item)

print(result)