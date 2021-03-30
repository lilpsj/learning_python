'''
내장함수 : 프로그래밍 언어를 개발한 사람들이 만들어놓은 함수
print, input, list, range
언어에 내장되어 있으므로 별도의 처리 없이 바로 사용 가능
'''

'''
사용자정의 함수 : 나와 같은 개발자가 필요에 의해 만든 함수
언어에 내장되어있지 않으므로 별도의 처리(import)가 먼저 필요함
random
'''

# abs()
# slice()
# len()
# max()
# round() - 반올림

# 문자열과 관련된 내장함수
# chr() -> 정수를 문자로 변환하는 함수
# ord() -> 문자를 정수로 변환하는 함수
# eval(0) -> 문자열로 이루어진 연산을 해주는 함수
# format() -> 데이터를 원하는 형식의 문자열로 변환해주는 함수
'format 매서드와 다름!'
# str() -> 데이터를 문자열로 변환해주는 함수

'아스키코드 https://shaeod.tistory.com/228'
# 예제-chr함수를 사용해서 Z, !를 출력하세요
print(chr(90))
print(chr(33))
print(ord("A"), "\n")

# eval 활용
print(eval("1+1"))

num1 = 27
print(eval("num1 * 2"), "\n")

print(format(100000000000000, ","))

num2 = 1000
print("결과값은" + str(num2))

# 예제
print("계산식을 입력하세요 : ", end="")
expr = input()
print(type(expr))
print(expr + " = " +str(eval(expr)))
