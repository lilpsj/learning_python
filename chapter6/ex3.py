#if else 조건문
'''
if 조건 :
    코드1
    코드2
else :
    코드1
    코드2
'''

#예제1
print("오늘의 미세먼지 농도를 입력하세요", end="")

finDust = int(input())

if finDust >= 5:
    print("집에 있는다.")
else:
    print("밖에 나간다.", "/n")
'else = 그렇지 않다면 이라고 해석해야됌'

#예제2
print("가진 현금을 입력하세요", end="")

money = int(input())

if money >= 10000:
    print("택시를 타세요")
else:
    print("버스를 탄다", "\n")

#예제3
print("비가 오면1, 오지않으면 0을 입력하세요")

isRaining = int(input())

if isRaining == 1:
    print("우비를 입는다")
else:
    print("선글라스를 끼세요", "\n")


#예제4
print("숫자를 입력하세요")
number = int(input())

if number % 2 == 0:
    print("2 * 1 =  ", "%d" % (2 * 1))
    print("2 * 1 =  ", "%d" % (2 * 2))
    print("2 * 1 =  ", "%d" % (2 * 3))
    print("2 * 1 =  ", "%d" % (2 * 4))
    print("2 * 1 =  ", "%d" % (2 * 5))
else:
    print("3 * 1 = ", "%d" % (3 * 1))
    print("3 * 1 = ", "%d" % (3 * 2))
    print("3 * 1 = ", "%d" % (3 * 3))
    print("3 * 1 = ", "%d" % (3 * 4))
    print("3 * 1 = ", "%d" % (3 * 5), "\n")

#예제5
print("1. 입력: ", end="")
number1 = int(input())
number2 = int(input())

if number1 > number2:
    print(number1)
else:
    print(number2, "\n")

#예제6
# 123 입력
# 213 입력
# 231 입력
