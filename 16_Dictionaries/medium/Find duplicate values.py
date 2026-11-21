# Find duplicate values

data = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 20,
    "e": 40,
    "f": 10
}

duplicates = []

for value in data.values():

    if list(data.values()).count(value) > 1:

        if value not in duplicates:
            duplicates.append(value)

print("Duplicate Values:", duplicates)