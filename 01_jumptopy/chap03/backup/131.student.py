# coding: cp949
marks = []

number = 1

print("<<�л� ���� �� ���α׷�>>")

while number<=5:
    mark = input(str(number)+"�� �л� ������ �Է��ϼ���: ")
    marks.append(int(mark))
    number = number +1

print("\n* �� ���")
number =1
for mark in marks:
    if mark > 60:
        print("%d�� �л� %d��, �հ��Դϴ�."%(number,mark))
    else:
        print("%d�� �л� %d��, ���հ��Դϴ�."%(number,mark))

    number = number+1
    
