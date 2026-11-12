# Create a formatted employee profile

name = input("Enter Employee Name : ")
age = int(input("Enter Employee Age : "))
department = input("Enter Department : ")
salary = float(input("Enter Salary : "))
city = input("Enter City : ")


print("\n====== EMPLOYEE PROFILE ======")

print(f"Employee Name : {name}")
print(f"Age           : {age}")
print(f"Department    : {department}")
print(f"Salary        : ₹{salary:.2f}")
print(f"City          : {city}")

print("==============================")