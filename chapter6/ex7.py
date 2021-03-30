#반복분(while) - break
'''
-반복문의 흐름을 조절할때 사용
-반복문의 조건식을 만족하기 전에 끝내고 싶을 때
-반복문을 끝내는 조건이 두개가 되는 것
'''

print("충전금액 :", end="")
money = int(input())
price = 2700

while money >= price:
    #break  키워드를 만나는 순간
    #break 키워드가 속한 반복문에서 빠져나감
    if money < price:
        break
    money = money - price

    print("잔액 : %d" % money)

print("프로그램 종료", "\n")

#예제2
import random

nansu = [False, False, False, False, False, True,False, False, False, False]
cutDown = False
hit = 0

'''
while cutDown != True:
    cutDown = random.choice(nansu)

    if cutDown:
        print("나무를 쓰러뜨렸다.", "\n")
    else:
        hit += 1
        print("나무를 {0}번 찍었다.". format(hit))

    if hit >= 10:
        break
'''

while True:
    cutDown = random.choice(nansu)

    if cutDown:
        print("나무를 쓰러뜨렸다.", "\n")
    else:
        hit += 1
        print("나무를 {0}번 찍었다.". format(hit))

    if cutDown >= True:
        break
    elif hit >= 10:
        break
