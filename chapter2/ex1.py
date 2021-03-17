'''
변수 선언 - RAM 내 데이터를 저장하기 위한 공간에 별명을 붙여주는 것
데이터를 관리하기 위해 메모리 주소를 사용하지 않고 내가 붙인 별명으로 데이터를 관리할 수 있음
'''

'''
1.영문자(대, 소문자 구분), 숫자, _(언더바)
2.첫 자리에는 숫자를 사용할 수 없다.
3.키워드는 변수명으로 사용할 수 없다.
'''

# 일반적인 프로그래밍 언어들은 선언과 값의 저장을 따로 할 수 있지만
# 파이썬은 선언과 동시에 값을 저장해야한다.(값을 할당한다 or 초기화시킨다)
# 변수 선언
value1 = 10

monja = "안녕하세요!"

average = 75.54

add = 123

majorVersion = "1.0"

minor_version = 0.4

'''
              RAM
주소 : Ox01FA8830(value1) 값 : 10
주소 : Ox01FA8831(monja) 값 : "안녕하세요"
주소 : Ox01FA8832(average) 값 : 75.54
'''

#print("value1 =",value1)
#print("monja =",monja)
#print("average =",average)
#print("minor_version =",minor_version)

name = "Alice"
age = 25
address = "우편번호 12345 서울시 영등포구 여의도동 서울빌딩 501호"
height = 168.5

print("name =", name)
print("age =", age)
print("address =", address)
print("height =", height)

