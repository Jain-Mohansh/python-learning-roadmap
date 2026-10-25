# Create a grade calculator
'''
Grade Criteria:

    Marks 90-100  → Grade A
    Marks 80-89   → Grade B
    Marks 70-79   → Grade C
    Marks 60-69   → Grade D
    Marks 40-59   → Grade E
    Marks 0-39    → Grade F
'''
marks = int(input('Enter your marks(/100) : '))
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
elif marks >= 40:
    grade = 'E'
else:
    grade = 'F'

print(f'For Your marks : {marks}\nYour Grade is {grade}')