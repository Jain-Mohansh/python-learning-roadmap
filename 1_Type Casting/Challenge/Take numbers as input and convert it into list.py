# Take "10 20 30 40 50" as input and convert it into [10, 20, 30, 40, 50]
numbers = []
for i in range(5):
    numbers.append(int(input(f'Enter the number {i+1} : ')))

print(numbers)