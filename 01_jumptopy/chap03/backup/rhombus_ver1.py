#coding: cp949

print("������ ��� ���α׷� ver1.0")

OddNum = int(input("Ȧ���� �Է��ϼ���(0 <- ���� : "))
i =1
blank =int(OddNum/2)


if OddNum == 0:
    print("���α׷��� ���� �Ǿ����ϴ�.")

while i <= OddNum:
    if OddNum%2 == 0:
        print("�߸� �Է� �Ͽ����ϴ�")
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
        print("�߸� �Է� �Ͽ����ϴ�.")
        break
    else:
        print(' '*blank,end='')
        


