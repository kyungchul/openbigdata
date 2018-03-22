# coding: cp949
marks = []

number = 1

print("<<학생 시험 평가 프로그램>>")

while number<=5:
    mark = input(str(number)+"번 학생 점수를 입력하세요: ")
    marks.append(int(mark))
    number = number +1

print("\n* 평가 결과")
number =1
for mark in marks:
    if mark > 60:
        print("%d번 학생 %d점, 합격입니다."%(number,mark))
    else:
        print("%d번 학생 %d점, 불합격입니다."%(number,mark))

    number = number+1
    
