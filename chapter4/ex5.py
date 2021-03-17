"""
논리 연산자 - 논리값(bool)을 연산하는 연산자
논리값 - True, False 2개

True -  참, 1
False - 거짓, 0 (이라고 하기도 함)

True 또는 False 논리 연산 True 또는 False

1.and - 두 값 모두 T 일 때 결과가 T (그리고)
and = 논리곱
1*1=1 = T
1*0=0 = F

2.or - 두 값 중 하나만 T이면 결과가 T (또는)
or = 논리합
1+1=1
1+0=1
0+1=1
0+0=0

3.not - 결과를 반대로 바꾸는 연산자
"""

print(True and True)
print(True and False)
print(False and True)
print(False and False, "\n")

print(True or True)
print(True or False)
print(False or True)
print(False or False, "\n")

print(not True)
print(not False)
print(not (True and True), "\n")

#예제
print("국어성적 : ", end="")
kor = int(input())

"input 입력시 오타확인용"
print(kor >= 0)
print(kor <= 100, "\n")

"같은 말 다른코드"
print(kor >= 0 and kor <= 100)

"파이썬에서만 적용되서 좋은 코드는 아님"
print(0 <= kor <= 100)

result1 = kor < 0
result2 = kor > 100
result = result1 or result2
print("or썻을때 : ", result)

#예제
result3 = kor < 0
result4 = kor > 100
result = not(result3 or result4)
print("or에 not 썼을때 : ", result, "\n")

#예제
#숫자를 입력 받아  var 변수에 저장하고
#짝수면 True 홀수면 False 출력

var = int(input())
print(var % 2 == 0)

body = float(input())
print(body >= 36.5)
