'''
문자열(str)
문자 - 하나의 문자
문자열 - 둘 이상의 문자들의 집합
'''

'''
문자열생성방법
1. '문자열' : 한줄짜리 문자열 생성
2. "문자열" : 한줄짜리 문자열 생성
3. ''' ''' : 여러줄짜리 문자열 생성
4. """ """ : 여러줄짜리 문자열 생성
4가지인 이유는 문자열 안에 특수문자가 들어갈 수 있으므로 특수문자를 쉽게 표현하기 위해서

monja5 = "호랑이가 "떡 하나 주면 안 잡아먹지"라고 했다. (인식못함)"
monja5 = "호랑이가 \"떡 하나 주면 안 잡아먹지\"라고 했다. (인식하는데 귀찮음)"
monja5 = '호랑이가 "떡 하나 주면 안 잡아먹지"라고 했다. (정답)'
'''

value1 = '어제는 비가 내려 시원했습니다.'
print(value1)

value2 = """"문자"는 홀따옴표(')와 쌍따옴표(")를 사용해서 저장할 수 있습니다."""
print(value2)

value3 = "파이썬 두번째 시간입니다."
print((value3), "\n")

#예제 - 문자열 생성
ex1 = '''오늘은
양력 2020년 7월 5일입니다.
음력 2020년 5월 15일입니다.'''
print((ex1), "\n")

exT = "오늘은\n양력 2020년 7월 15일입니다.\n음력 2020년 5월 15일입니다."
print((ex1), "\n")

ex2 = """Life is too short
You need python"""
print((ex2), "\n")