# coding: cp949

prompt="""
1. 추가
2. 삭제
3. 리스트
4. 종료


숫자를 입력하세요: """

number=0

while number !=4:
    number = int(input(prompt))
if number == 1:
    print("'1추가' 메뉴를 선택하였습니다")
if number == 2:
    print("삭제를 선택함")
if number == 3:
    print("리스트를 선택함")
if number == 4:
    print("'1,2,4'만 지원한다")
    
