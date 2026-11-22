# Create nested dictionaries for multiple students

students = {
    101: {
        "name": "Rahul",
        "age": 20,
        "marks": 85
    },

    102: {
        "name": "Priya",
        "age": 19,
        "marks": 90
    },

    103: {
        "name": "Amit",
        "age": 21,
        "marks": 78
    }
}

# Display all students
for roll, details in students.items():
    print("\nRoll Number:", roll)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Marks:", details["marks"])