# Create calculate_average(numbers)

def calculate_average(*args):
    summ = 0
    for i in args:
        summ += i
    average = summ / len(args)
    return(average)


print(calculate_average(2,2))