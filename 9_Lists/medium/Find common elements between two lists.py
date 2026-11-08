# Find common elements between two lists

fruits = ['Apple', 'Banana', 'Kiwi', 'Mango', 'Tomato']
Vegetables = ['Potato', 'Ookra', 'Cilantro', 'Tomato']

for fruit in fruits:
    if fruit in Vegetables:
        print(f'Common element : {fruit}')