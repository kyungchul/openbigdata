#coding: cp949

print ("나이에 따른 등급,요금 결제유형 프로그램 _ver4")

age = int(input("나이를 입력하세요: "))
choice = int(input("i요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용 카드) "))
kid = 2000
teen = 3000
adult = 5000
i = 0

free_ticket = 3
dis_ticket = 5

while True:
    if choice == 1:
        if age < 0:
            print("다시 입력하세요")
        elif age <4:
            print("귀하는 유아 등급이며 요금은 무료 입니다")
        elif age >=4 and age <14:
            print("귀하는 어린이 등급이며 요금은 2000원 입니다")
            charge = int(input("요금을 입력하세요 : "))
            if charge < kid:
                print("%d가 모자랍니다. 입력하신 %d를 반환합니다."%(kid-charge,charge))
            elif charge ==kid:
                print("감사합니다. 티켓을 발행합니다.")
            elif charge > kid:
                print("감사합니다. 티켓을 발행하고 거스릅돈 %d를 반환합니다." %(charge-kid))
        elif age >=14 and age <19:
            print("귀하는 청소년 등급이며 요금은 3000원 입니다.")
            charge = int(input("요금을 입력하세요 : "))
            if charge < teen:
                print("%d가 모자랍니다. 입력하신 %d를 반환합니다."%(teen-charge,charge))
            elif charge == teen:
                print("감사합니다. 티켓을 발행합니다.")
            elif charge > teen:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." %(charge-teen))
        elif age >19 and age<66:
            print("귀하는 성인 등급이며 요금은 5000원 입니다.")
            charge = int(input("요금을 입력하세요 : "))
            if charge < adult:
                print("%d가 모자랍니다. 입력하신 %d를 반환합니다." %(adult-charge,charge))
            elif charge == adult:
                print("감사합니다. 티켓을 발행합니다.")
            elif charge > adult:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." %(charge-adult))
        elif age>= 66:
            print("귀하는 노인 등급이며 요금은 무료입니다.")
   
    if choice == 2:
        if age>=4 and age<14:
            print("결제 금액이 할인되어 %d원 결제 되었습니다. 티켓을 발행합니다." %(kid-(kid*0.1)))
        elif age>=14 and age<19:
            print("결제 금액이 할인되어 %d원 결제 되었습니다. 티켓을 발행합니다." %(teen-(teen*0.1)))
        elif age>=19 and age<60:
            print("결제 금액이 할인되어 %d원 결제 되었습니다. 티켓을 발행합니다." %(adult-(adult*0.1)))
        elif age>=60 and age<66:
            print("결제 금액이 할인되어 %d원 결제 되었습니다. 티켓을 발행합니다." %(adult-(adult*0.15)))
                 
    
    
    i= i+1



#    if i%7==0 and free_ticket>0 or i%4 ==0 and dis_ticket >0 :
#        print("축하합니다 무료 티켓이 배분되었습니다 (남은 티켓 %d)", free_ticket)
#        free_ticket = free_ticket -1
#        print("축하합니다 할인 티켓이 배분되었습니다 (남은 티켓 %d)", dis_ticket)
#        dis_ticket = dis_ticket -1
#    i = i+1


