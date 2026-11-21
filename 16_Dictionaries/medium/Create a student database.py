# Create a student database

students = {
    101: {"name": "Rahul", "age": 20, "marks": 85},
    102: {"name": "Priya", "age": 19, "marks": 92},
    103: {"name": "Amit", "age": 21, "marks": 78}
}

for roll_no, details in students.items():
    print("Roll No:", roll_no)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Marks:", details["marks"])
    print("----------------")

students[104] = {
    "name": "Neha",
    "age": 20,
    "marks": 90
}

roll = 102

if roll in students:
    print("Student Found:", students[roll])
else:
    print("Student Not Found")