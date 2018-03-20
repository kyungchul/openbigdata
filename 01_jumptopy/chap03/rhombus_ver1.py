#coding: cp949

print("마름모 출력 프로그램 ver1.0")

OddNum = int(input("홀수를 입력하세요(0 <- 종료 : "))
i =1
blank =int(OddNum/2)


if OddNum == 0:
    print("프로그램이 종료 되었습니다.")

while i <= OddNum:
    if OddNum%2 == 0:
        print("잘못 입력 하였습니다")
        break
    else:
        print(' '*blank,end='')
        print('*'*i)
        i = i+2
        blank = blank-1
i -=2
blank +=1

while i >=0:
    if OddNum%2 == 0:
        print("잘못 입력 하였습니다.")
        break
    else:
        print(' '*blank,end='')
        


