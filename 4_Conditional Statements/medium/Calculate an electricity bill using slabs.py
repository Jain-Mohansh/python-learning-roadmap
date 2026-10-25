# Calculate an electricity bill using slabs
'''A common example slab structure is:

    First 100 units → ₹2 per unit

    Next 100 units (101-200) → ₹3 per unit

    Next 200 units (201-400) → ₹5 per unit

    Above 400 units → ₹7 per unit
'''
units = int(input('Enter the electricity units used : '))
if units <= 100:
    bill = units * 2
elif units <=200:
    bill = 100 * 2 + (units-100) * 3
elif units <= 400:
    bill = 100 * 2 + (100 * 3) + ((units - 200) * 5)
else:
    bill = 100 * 2 + (100 * 3) + (200 * 5) + (units - 400) * 7

print(bill)