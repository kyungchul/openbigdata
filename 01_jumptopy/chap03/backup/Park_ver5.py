#coding: cp949

print ("���̿� ���� ���,��� �������� ���α׷� _ver4")

age = int(input("���̸� �Է��ϼ���: "))
choice = int(input("��� ������ �����ϼ���. (1: ����, 2: ���� ���� �ſ� ī��) "))
kid = 2000
teen = 3000
adult = 5000

free_ticket = 3
discount_ticket = 5
number = 1
 
if choice == 1:
            if age<0:
                print("�ٽ� �Է��ϼ���")
            elif age<4:
                print("���ϴ� ���� ����̸� ����� ���� �Դϴ�")
            elif age>=4 and age<14:
                print("���ϴ� ��� ����̸� ����� 2000�� �Դϴ�")
                charge = int(input("����� �Է��ϼ��� : "))
                if charge < kid:
                    print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�."%(kid-charge ,charge))
                while True: 
                    if number%7 ==0:
                         print("�����մϴ�. ���ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�.���� ����Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��" %free_ticket)
                         number = number +1
                         free_ticket = free_ticket -1
                    elif number%4 ==0:
                         print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��" %discount_ticket)
                         number = number +1
                         discount_ticket = distikcet -1
                         continue

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
                    print("���ϴ� ���ε���̸� ����� �����Դϴ�.")
     

if choice == 2:

    if age>=4 and age<14:
        print("���� �ݾ��� ���εǾ� %d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %(kid-(kid*0.1)))
    elif age>=14 and age<19:
        print("���� �ݾ��� ���εǾ� %d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %(teen-(teen*0.1)))
    elif age>=19 and age<60:
        print("���� �ݾ��� ���εǾ� %d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %(adult-(adult*0.1)))
    elif age>=60 and age<66:
        print("���� �ݾ��� ���εǾ� %d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %(adult-(adult*0.15)))
                 
 

