#함수
'''
함수를 만드는 방법 (정의, 선언)
 def 함수이름(매개변수):
    코드1
    코드2
    ...
    코드n

매개변수 - 함수가 동작하는데 필요한 재료
매개변수는 있을수도 있도 없을수도 있음
'''


#반복되는 코드지만 반복문 사용안됌. 왜? 변수명이 다 다르기 때문
'''
while True:
    print("첫번째 학생의 국어 점수 : ", end="")
    kor1 = int(input())
    if 0 <= kor1 and kor1 <= 100:
        break
    else:
        print("0~100점 사이로 입력해주세요")

print("두번째 학생의 국어 점수 : ", end="")
kor2 = int(input())

print("세번째 학생의 국어 점수 : ", end="")
kor3 = int(input())

print("네번째 학생의 국어 점수 : ", end="")
kor4 = int(input())

print("다섯번째 학생의 국어 점수 : ", end="")
kor5 = int(input())

코드변화 : 변수하나하나 적기 -> 변수 하나당 whilt반복문 사용 -> 함수사용
'''

def inputKor():
    while True:
        print("국어 점수 : ", end="")
        kor1 = int(input())
        if 0 <= kor1 and kor1 <= 100:
            break
        else:
            print("0~100점 사이로 입력해주세요", "\n")
    return kor1

kor1 = inputKor()

'''
#함수 예제
def sayHello():
    print("안녕하세요")

# sayHello 라는 이름의 함수를 '호출'
# 함수를 사용할 때 ()는 매개변수 자리
# sayHello 함수를 정의할 때 매개변수를 비워뒀으므로
# 함수를 호출할 때도 매개변수 자리는 비워둔다
sayHello()
'''

#예제1
def welcome():
    print("Hello Python")
    print("Nice to meet you")
    print("=" * 10, "\n")

for i in range(3):
    welcome()

#예제2
def add():
    print(1+1, "\n")

add()

#예제3
def gugudan():
    forward = 2
    for backward in range(1, 10):
        result = forward * backward
        print("%d * %d = %d" % (forward, backward, result), "\n")

gugudan()

#예제4
def addOrIn():
    num = int(input())
    if num % 2 == 0:
        print((num), "= 짝수", end="")
    else:
        print((num), "= 홀수", end="")
    #if 17 % 2 == 0:

addOrIn()
'''
처리과정
1.def addOrIn(): addOrIn()함수를 정의하네, 매개변수없음
2.int(input)을 변수 num에 저장
3.num을 2로 나눴을때 나머지가 0일 떄
4.num= 짝수라고 출력
5.나머지가 0이 아니면
6.num=  홀수라고 출력
7.addOrIn 함수호출
8.만약
'''