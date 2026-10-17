# Take comma-separated marks and calculate their average
marks = input('Enter your marks (using ",") : ' )
marks_list = [int(i) for i in marks.split(',')]
print(marks_list)
average = sum(marks_list)/len(marks_list)
print('average = ' ,average)