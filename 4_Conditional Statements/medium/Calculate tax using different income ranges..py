# Calculate tax using different income ranges.
'''
Tax Slabs (Example for Practice):

    Income up to ₹3,00,000        → 0% tax

    Income ₹3,00,001-₹6,00,000    → 5% tax

    Income ₹6,00,001-₹10,00,000   → 10% tax

    Income above ₹10,00,000       → 20% tax
'''

annual_income = int(input('Enter your annual income : '))

if annual_income <= 300000:
    tax = annual_income * (0/100)
elif annual_income <= 600000:
    tax = 300000 * (0/100) + (annual_income-300000) * (5/100)
elif annual_income <= 1000000:
    tax = 300000 * (0/100) + (300000) * (5/100) + (annual_income-600000) * (10/100)
else:
    tax = 300000 * (0/100) + (300000) * (5/100) + (400000) * (10/100) + (annual_income - 1000000) * (20/100)

print(f'Your tax amount for {annual_income} annual income is {tax}')