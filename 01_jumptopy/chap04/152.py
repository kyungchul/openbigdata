def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d입니다." %old)

    if man:
        print("남자 입니다.")
    else:
        print("여자 입니다.")

say_myself("박응용", 27)
say_myself("이효리",34,False)
say_myself("안철수",56,True)
