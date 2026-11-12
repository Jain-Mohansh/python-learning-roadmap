# Display percentages using f-strings

marks = float(input("Enter Your Marks : "))
total = float(input("Enter Total Marks : "))

percentage = (marks / total) * 100

print(f"Your Marks : {marks}/{total}")
print(f"Percentage : {percentage:.2f}%")