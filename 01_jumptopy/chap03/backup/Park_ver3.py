#coding: cp949

print("���̿� ���� ���, ����� ��� ���α׷� _ver3")

age = int(input("���̸� �Է��ϼ���: "))
kid = 2000  
teen= 3000 
adult = 5000

if age<0:
    print("�ٽ� �Է��ϼ���")
elif age<4:
    print("���ϴ� ���� ����̸� ����� ���� �Դϴ�")
elif age>=4 and age<14:
    print("���ϴ� ��� ����̸� ����� 2000�� �Դϴ�")
    charge = int(input("����� �Է��ϼ��� : "))
    if charge < kid:
        print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�."%(kid-charge ,charge))
    elif charge == kid:
        print("�����մϴ�. Ƽ���� �����մϴ�.")
    elif charge > kid:
        print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %(charge-kid))
elif age>=14 and age<19:
    print("���ϴ� û�ҳ� ����̸� ����� 3000�� �Դϴ�")
    charge = int(input("����� �Է��ϼ��� : "))
    if charge < teen:
        print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�."%(teen-charge, charge))
    elif charge == teen:
        print("�����մϴ�. Ƽ���� �����մϴ�.")
    elif charge > teen:
        print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�."%(charge-teen))
elif age>=19 and age<66:
    print("���ϴ� ���� ����̸� ����� 5000�� �Դϴ�")
    charge = int(input("����� �Է��ϼ��� : "))
    if charge < adult:
        print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�."%(adult-charge,charge))
    elif charge == adult:
        print("�����մϴ�. Ƽ���� �����մϴ�.")
    elif charge > adult:
        print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %(charge-adult))
elif age>=66:
    print("���ϴ� ���ε���̸� ����� �����Դϴ�")





