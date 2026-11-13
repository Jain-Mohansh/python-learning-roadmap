# Document function parameters

def rect_area(length, breadth):
    '''The function has two parameters
    [length] type<int> : Takes the length of the rectangle
    [breadth] type<int> : Takes the bradth of the rectangle'''
    area = length * breadth
    return area

print(rect_area.__doc__)
print(rect_area(2,3))