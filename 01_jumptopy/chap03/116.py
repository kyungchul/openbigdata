#coding: cp949
x=1
y=1
z=1

print("x: "+str(x)+" y: "+str(y)+", z:"+str(z))  #z�� ��� �� �� �ֵ��� ����                                                  ��Ʈ��(63 page)���� ����

input_str=("x: {0}, y: {1}. z:{2}".format(x,y,z))
print(input_str)
print("x: {0}, y: {1}. z:{2}".format(x,y,z))

if x or y:
    print("if x or y: ���� ����")
else:
    print("if x or y: ���� �Ҹ���")

if x and y:
    print("if x and y: ���� ����")
else:
    print("if x or y: ���� �Ҹ���")

if not x:
    print("not x ���� ����")
else:
    print("not x ���� �Ҹ���")

if not y:
    print("not y ���� ����")
else:
    print("not y ���� �Ҹ���")

if x and y and z: #�Ʒ� ������ ������ �� �ִ� x,y,z ���� ������ ��
    print("x and y and z: ���� ����")
else:
    print("x and y and z: ���� �Ҹ���")
if x or y or z:
    print(" x or y or z: ���� ����")
else:
    print(" x or y or z: ���� �Ҹ���")

