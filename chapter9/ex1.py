# 클래스
# c언어에는 클래스가 없다 = 굳이 클래스 없어도 프로그래밍이 가능
# Calculator 클래스를 정의(선언)했다

class Calculator:
    # 계산기를 위한 클래스
    # 속성 - 값1, 값2, 연산자, 연산 결과
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.op = ["+", "-", "*", "/"]
        self.result = 0
        self.color = 0
        self.brand = 0

    # 기능 - 더하기, 빼기, 곱하기, 나누기, ...
    def add(self, num1, num2):
        return num1 + num2

    def minus(self, num1, num2):
        return num1 - num2

# Calculator() -> 클래스의 인스턴스를 만든다
# 클래스의 인스턴스를 만든다 = 쿠키 틀은 먹을 수 없고, 쿠키 틀로 찍어낸 쿠키를 먹을 수 있는 것처럼
# 클래스를 정의해뒀다고 해서 그 클래스를 바로 사용할 수 있는 건 아님
# 클래스의 인스턴스를 만들어야지 클래스 안에 정의해둔 속성(멤버 변수)와 기능(멤버 메서드)을 사용할 수 있다.

# redCal 객체
redCal = Calculator()
redCal.num1 = 10
redCal.num2 = 24
redCal.add(1, 1)

# blueCal 객체
blueCal = Calculator()
blueCal.color = "blue"
blueCal.add(1, 2)

# blackCal 객체
blackCal = Calculator()
blackCal.color = "black"

'''
밑에 코드의 문제점
number1, number2, op, result = 계산기를 위한 변수
add, minus = 계산기를 위한 함수

짜다보면 반복되는 것이 나옴
연관있는 변수와 연관있는 함수를 하나로 묶는 방법 ==> 클래스

클래스로 묶은 변수 = 요소, 속성, 멤버 변수(in 객체지향 프로그래밍언어)
클래스로 묶은 함수 = 기능, 함수, 멤버 메서드(in 객체지향 프로그래밍언어)

클래스만 있다면 똑같은 속성과 기능을 갖고 있는 객체를 만들 수 있다.
'''

print("===== 계산기 =====")
print("연산하고자 하는 두 수를 입력 후")
print("연산자를 입력하세요")
print("연산은 +, -, *, / 만 가능합니다")
print("프로그램을 종료하려면 연산자에 0을 입력하세요")
print("===== ===== =====")

def add(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2

# 연산한 결과를 누적해서 가지고 있을 수 있도록 변수생성
result = 0

# while문 흐름만 나열
# 실제 핵심적인 역할은 함수가 할 수 있도록 짜기
while True:
    print("입력1 : ", end="")
    number1 = int(input())

    print("입력2 : ", end="")
    number2 = int(input())

    print("연산자 : ", end="")
    op = input()

    if op == "0":
        break

    if op == "+":
       result = result + add(number1, number2)
    elif op == "-":
        result = result + minus(number1 - number2)

    print(result)
