# coding: cp949
#pocket = ['paper','cellphone','money']
#pocket = ['paper','cellphone']
pocket=[]

item=input("���Ͽ� �������� ì�⼼��: ")
pocket.append(item)

if'card' in pocket:
    print("�ſ�ī��� �ýø� Ż���� ��õ�մϴ�")
elif 'money' in pocket:
    print("���� �̿�� �������� �� ì�⼼��.")
elif 'cellphone' in pocket:
    print("����Ʈ���� ����ī�� ����� �ִ��� Ȯ���ϼ���")
else:
    pass

