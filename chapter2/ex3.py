'''
기본 데이터 타입
1.int : 정수
2.float : 실수
3.bool : 논리(True)
4.str : 문자열
'''

# 지정 대상의 데이터 타입을 알려주는 기능
'''type()'''
print(type(25))
print(type(168.5))
print(type("ALICE"))
print(type(True))

name = "Alice"
age = 25
height = 168.5
print(type(name))
print(type(age))
print(type(height))

type(25)
'''type에 입력한거라서, float나오는게 맞음'''

print("나이: ", end="")
age = input()
print(type(age))
'''25넣었는데 왜 str이냐면 input은 입력된 데이터는 모두 문자열 타입'''


# 예제1
# 나이를 입력하는 부분
print("!! 나이를 입력하면 태어난 연도를 알려드립니다 !!")
print("나이(만) :", end="")

age = input()

# 나이에 따른 태어난 연도를 계산하는 부분
# year = 2021 - (age)
# 같은 타입의 데이터끼리만 처리됨, 2021=int <-> age=str이라서 Err

year = 2021 - int(25)
"""
int(n) -> n을 정수로 변환
float(n) -> n을 실수로 변환
bool -> n을 논리로 변환
str -> n을 문자열로 변환
(list, tuple), dic, set 등등
"""
# 문자열, 실수, 논리를 정수화
var1 = int(26)
var2 = int(3.14)
var3 = int(True)

# 문자열, 정수, 논리를 실수화
var4 = float(3.14)
var5 = float(26)
var6 = float(True)

print(type(var1))
print(type(var2))
print(type(var3))

# 계산 결과를 출력하는 부분
print(age, "살의 태어난 연도는 ", year, "년입니다.")

# 예제2
print("어제의 기온 :", end="")
yesterday_temp = input()
print("오늘의 기온 :", end="")
today_temp = input()

yesterday_temp = int(yesterday_temp)
today_temp = int(today_temp)

temp_diff = yesterday_temp - today_temp

print("어제와 오늘의 기온차는 ", temp_diff, "도 입니다")