# Build a student management system

students = {}

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))

        students[roll] = {
            "name": name,
            "marks": marks
        }

        print("Student added successfully!")

    elif choice == 2:
        for roll, details in students.items():
            print("Roll Number:", roll)
            print("Name:", details["name"])
            print("Marks:", details["marks"])

    elif choice == 3:
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            print("Name:", students[roll]["name"])
            print("Marks:", students[roll]["marks"])
        else:
            print("Student not found!")

    elif choice == 4:
        print("Exiting Student Management System.")
        break

    else:
        print("Invalid choice!")