# Sort a dictionary by values

marks = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Neha": 95
}

sorted_dict = dict(
    sorted(marks.items(), key=lambda item: item[1])
)

print(sorted_dict)