import sys
# run -> edit configuration -> parameter에서 값 aaa,bbb,ccc
args = sys.argv[1:]

for i in args:
    print(i.upper(), end=' ')

# print(sys.argv[1])