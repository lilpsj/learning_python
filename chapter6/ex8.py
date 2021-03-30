#예제1
import random

dice = 0
diceCount = 0
while True:
    dice = random.randint(1, 8)
    diceCount += 1

    print("dice = %d / diceCount = %d" % (dice, diceCount), "\n")

    if dice == 5 or diceCount == 8:
        break

#예제2
price = 300
amountCoffee = 10

print("돈 투입 :", end="")

money = int(input())

while True :
    amountCoffee -= 1
    money -= price
    if amountCoffee == 0:
        print("믹스커피가 부족합니다. 반환되는 잔액은 %d입니다." % money)
        break
    if money < 300:
        print("잔액이 부족합니다. 반환되는 잔액은 %d 원입니다." % money)
