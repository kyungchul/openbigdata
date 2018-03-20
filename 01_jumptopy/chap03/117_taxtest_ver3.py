#coding: cp949

money=int(input("가지고 계신 금액을 입력하세요 : "))
card=int(input("신용카드를 가지고 계십니까? (1:예, 2:아니오)")

print("입력 조건 분석")
print("현재 가지고 계신 금액은 "+str(money)+"원 입니다"))

if card:
    print("신용카드를 소지하고 계십니다")
else:
    print("신용카드가 없습니다.")

print("분석결과")
if money >=3000 or card==1:
    print("택시를 타고 가실 수 있음")
else:
    print("걸어가")




