#coding: cp949

money=int(input("������ ��� �ݾ��� �Է��ϼ��� : "))
card=int(input("�ſ�ī�带 ������ ��ʴϱ�? (1:��, 2:�ƴϿ�)")

print("�Է� ���� �м�")
print("���� ������ ��� �ݾ��� "+str(money)+"�� �Դϴ�"))

if card:
    print("�ſ�ī�带 �����ϰ� ��ʴϴ�")
else:
    print("�ſ�ī�尡 �����ϴ�.")

print("�м����")
if money >=3000 or card==1:
    print("�ýø� Ÿ�� ���� �� ����")
else:
    print("�ɾ")




