# Find common elements between lists

num1 = [1,2,3,4,2,6,7]
num2 = [4,3,2,6,8,9,0]

print(f"{num1=}")
print(f"{num2=}")

common_elements = list(set(num1)&set(num2))

print(f"{common_elements=}")
