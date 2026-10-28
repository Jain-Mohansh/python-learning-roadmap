# Print a month based on a number
# Print a day based on a number
number = int(input('Enter the day number : '))

match number:
    case 1:
        print('january')
    case 2:
        print('February')
    case 3:
        print('march')
    case 4:
        print('April')
    case 5:
        print('May')
    case 6:
        print('June')
    case 7:
        print('July')
    case 8:
        print('August')
    case 9:
        print('September')
    case 10:
        print('October')
    case 11:
        print('November')
    case 12:
        print('December')
    case _:
        print('Invalid Choice !')