import random

nansu = [False, False, False, False, False, True,False, False, False, False]
cutDown = False
hit = 0

while cutDown != True:
    cutDown = random.choice(nansu)

    if cutDown:
        print("나무를 쓰러뜨렸다.", "\n")
    else:
        hit += 1
        print("나무를 {0}번 찍었다.". format(hit))

#예제1
print("충전금액 : ", end="")
money = int(input())
price = 1350

"1350이상일 동안만 반복해라!"
while money >= price:
    money = money - price
    print("잔액 : %d" % money)
"price를 1350으로 대체해도됨, 근데 가격이 바뀌는 수정을 두번해줘야돼"
