# coding: cp949

print("�ý� �ȳ� ���̵� ���α׷� ver1")

#money=2000
#print("������ ��� �ݾ��� �Է��ϼ���: ",end='')
money=int(input("������ ��� �ݾ��� �Է��ϼ���: "))
card =True

print("�Է� ���� �м�")
print("\n���� ������ ��� �ݾ��� "+str(money)+"�� �Դϴ�.")

if card:
    print("�ſ�ī�带 �����ϰ� ����")
else:
    print("���� �ſ�ī�� ����")

print("\n�м� ���")
if money >= 3000 or card:
    print("�ýø� Ÿ�� ���� �� �ֽ��ϴ�.")
else:
    print("�ɾ �ù߾�.")

print("\n���� �ý� �ȳ� ���α׷��� �̿��� �ּż� �����մϴ�")
