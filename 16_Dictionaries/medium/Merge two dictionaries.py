# Merge two dictionaries

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "d": 40,
    "e": 50,
    "f": 60
}


merged = dict1.copy()


merged.update(dict2)

print("Merged Dictionary:", merged)