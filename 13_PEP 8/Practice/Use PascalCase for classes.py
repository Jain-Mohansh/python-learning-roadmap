# Use PascalCase for classes
# Create a student class

class StudentDetails:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Student Name : {self.name}")
        print(f"Student Age : {self.age}")


student = StudentDetails("Rahul", 20)

student.display_details()