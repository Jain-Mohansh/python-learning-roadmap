# Create a formatted student report

name = input("Enter Student Name : ")
roll_no = int(input("Enter Roll Number : "))

english = int(input("Enter English Marks : "))
maths = int(input("Enter Maths Marks : "))
science = int(input("Enter Science Marks : "))

total = english + maths + science
percentage = total / 3


print("\n========== STUDENT REPORT ==========")

print(f"Student Name : {name}")
print(f"Roll Number  : {roll_no}")

print("------------------------------------")

print(f"English Marks : {english}")
print(f"Maths Marks   : {maths}")
print(f"Science Marks : {science}")

print("------------------------------------")

print(f"Total Marks  : {total}/300")
print(f"Percentage   : {percentage:.2f}%")

print("====================================")
print("          BEST OF LUCK!")