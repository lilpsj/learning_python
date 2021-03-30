#멤버 연산자 실습
'''
pocket = ['paper', 'cellphoen', 'money']
money = 'money' in pocket
card = True

if money:
    print("택시를 타고 가라")

else:
    if card:
       print("택시를 타고 가라")
    else:
       print("걸어가라")
'''

'''is elif else
if조건1
    코드1
    코드2
elif조건2
    코드1
    코드2
elif조건3
    코드1
    코드2
else:
    코드1
    코드2
'''

pocket = ['paper', 'cellphoen', 'money']
money = 'money' in pocket
card = True

if money:
    print("택시를 타고 가라")

elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라", "\n")

#예제1
pushButtonNumber = 1

if pushButtonNumber == 1:
    print("콜라")
elif pushButtonNumber ==2:
    print("사이다")
elif pushButtonNumber ==3:
    print("환타")
else:
    print("제공하지 않습니다", "\n")

#예제2
x = 10
y = 7

if x > y:
    print("x가 큽니다")
elif x < y:
    print("y가 큽니다")
elif x == y:
    print("x와 y가 동일합니다")

'''
elif를 else로 변경 가능
else:
    print("x와 y가 동일합니다")
'''

'''
소스코드의 최적화
각각의 if문으로만 예제2를 처리하면 3번 연산, if elif else 조건문으로 하면 1번에 처리가 됌
'''

