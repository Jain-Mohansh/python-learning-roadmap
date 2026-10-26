# Create a BMI calculator.
weight = float(input('Enter your weight (in kgs): '))
height = float(input('Enter your height (in meters): '))
bmi = weight / (height**2)
print(f'Your BMI is {bmi:.2f}')
if bmi < 18.5:
    print('Your are UnderWeight.')
elif bmi < 25:
    print('Your weight is Normal.')
elif bmi<30:
    print('You are OverWeight.')
else:
    print('You are Suffering from Obesity.')
