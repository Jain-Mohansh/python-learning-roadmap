# Ask for marks and calculate percentage

marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))
marks4 = float(input("Enter marks for subject 4: "))
marks5 = float(input("Enter marks for subject 5: "))

total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total / 500) * 100

print("Total Marks:", total)
print("Percentage:", percentage, "%")
