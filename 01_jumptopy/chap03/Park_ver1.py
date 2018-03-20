#coding: cp949

print("나이에 따른 입장료 계산 프로그램 ver1.0")

age = int(input("나이를 입력하세요 : "))

if age<4:
    print("무료입니다!")
elif age>=4 and age<14:
    print("2000원 입니다")
elif age>=14 and age<19:
    print("3000원 입니다")
elif age>=19 and age<66:
    print("5000원 입니다")
elif age>=66:
    print("무료입니다")


