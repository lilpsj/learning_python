'''
함수를 정의하는 방법 (정의, 선언)
 def 함수이름(매개변수):
    코드1
    코드2
    ...
    코드n

매개변수 - 함수가 동작하는데 필요한 재료
매개변수가 있는 함수
'''


#매개변수 없이1 더하기 1의 결과를 출력하는 함수
def add():
    print(1+1)

add()

#매개변수가 있는 1 더하기 1의 결과를 출력하는 함수
def add(num1, num2):
    print(num1 + num2)

# 함수를 호출할 때 매개변수 자리에 넣는 값을 인자라고 부름
# 1,1 두개의 인자를 넣어서 add 함수 호출
add(1,1)
add(1,0)
print("\n")
'''
#제어가 한손에1, 다른손에1을 들고  def add(num1, num2)로 올라가서 저장
#num1+num2에 있는 1과 1을 더해서 출력
#다시 제자리로 내려온뒤, 밑에줄 코드 실행

#예제1 - 태어난 연도를 입력받아 나이를 계산해 출력하는 함수
def calcAge():
    print("태어난 연도를 입력해주세요")
    birthYear = int(input())

    age = 2021 - birthYear
    print("%d 년도생은 나이가 %d살입니다." % (birthYear, age),"\n")

calcAge()
'''

"""
<docString - 함수를 설명하는 주석>
:param year: 태어난 연도 (parameter;매개변수) => 'year'매개변수에 대한 주석
:return: 없음 (함수 calcAge1)이 만들어내는 결과에 대한 주석
"""
# 매개변수 있게 만든것
def calcAge1(year):
    """

    :param year:
    :return:
    """
    age = 2021 - year
    print("%d 년도생은 나이가 %d살입니다." % (year, age), "\n")

print("태어난 연도 : ", end="")
year = int(input())
#매개변수명과 인자명이 같지 않아도 됨

calcAge1(year)

#예제3 - 두 정수 중 큰 수를 출력하는 함수를 만드세요
def compareNum(num1, num2):
    if num1 > num2:
       print(num1)
    else:
       print(num2)

compareNum(1, 2)
print("\n")

#예제4
def compare2(var):
    if var % 2 == 0:
        print("짝수", "\n")
    else:
        print("홀수", "\n")

compare2(17)

#예제5 -
def calcScore(kor, eng, mat):
    sum = kor + eng + mat
    avg = sum / 3
    print("합계 = %d, 평균 = %f" % (sum, avg),"\n")

print("국어점수 : ", end="")
korean = int(input())
print("영어점수 : ", end="")
english = int(input())
print("수학점수 : ", end="")
math = int(input())

calcScore(korean, english, math)


#예제6 두 정수 중 작은 수를 출력
def compareNum2(num1, num2):
    if num1 < num2:
        print(num1)
    else:
        print(num2)

print("두 정수 중 작은 수는?")
compareNum2(17, 25)
print()

'''
#예제7 세 정수 중 큰 수를 출력
def maximum(num1, num2, num3):
    # max -  큰 수
    max = num1

    if num2 > max:
        max = num2
    if num3 > max:
        max = num3

print("세 정수 중 최대값은?")
print("최대값은", max, " 입니다", "\n")

maximum(1,3,5)
'''

#예제8 네 정수 중 큰 수를 출력
def maximum4(var1, var2, var3, var4):
    # max -  큰 수
    max = var1

    if var2 > max:
        max = var2
    if var3 > max:
        max = var3
    if var4 > max:
        max = var4

    print(max)

num1 = 10
num2 = 20
num3 = 30
num4 = 40

maximum4(10, 20, 30, 40)
#복사가 된 인자(1,2,3,4)를 하나씩 가지고 매개변수로 올라감
#그 말인 즉슨, var1과 num1이 같은 값을 가지고 있는 변수일 뿐, 연결되어 있는 것이 아니다

#예제9
def swap(var1, var2):
    temp = var1
    var1 = var2
    var2 = temp

num1 = 10
num2 = 20

swap(num1, num2)
