'''
튜플
숫자, 문자열, 리스트와 같은 데이터의 한 종류
변수명 = (요소1, 요소2, 요소3 ...)  <-> 변수명 = [요소1, 요소2, 요소3] (리스트)
튜플 내 요소의 순서가 있고 데이터의 중복을 허용
리스트와 동일하게 사용하나 튜플은 값을 변경할 수 없다.
기준이 되는 값을 저장하는 용도 그래서 값을 변경할 수 없음

emptyTuple = ()

numberTuple = (1, 2, 3)

floatTuple = (3.14, 0.14, 0.34)

duplicatTuple = (1, 1, 1)

stringTuple = ("나는", "지금")

variousTuple = (1, "파이썬을", 2, "공부하고 있다")

complexTuple = ((1,2), 3, ("파", "이", "썬"))
#튜플에 리스트가 요소로 들어갈 수 있음
'''

numberTuple = (1, 2, 3)
print("인덱스0자리 튜플 : ", numberTuple[0])

#튜플 덧셈
oddTupple = (1, 3, 5, 7, 9)
evenTuple = 2, 4, 6, 8, 10
fullTuple = oddTupple + evenTuple
print(fullTuple)

#튜플 곱셈
#요소가 하나짜리인 튜플생성시 ,를 붙여줘야 인식함
multiTuple = (1,)

dashTuple = ("=", ) * 3
asteriskTuple = ("*", ) * 3
fullTuple1 = dashTuple + asteriskTuple
print(fullTuple1)

#튜플 인덱싱, 리버스인덱싱, 슬라이싱
numberTuple1 = (14, 75, 32, 94)
print(numberTuple1[0])
print(numberTuple1[1])
print(numberTuple1[2])
print(numberTuple1[3], "\n")

print(numberTuple1[-4])
print(numberTuple1[-3])
print(numberTuple1[-2])
print(numberTuple1[-1], "\n")

print(numberTuple1[1:3])
print(numberTuple1[:3])
print(numberTuple1[1:])
print(numberTuple1[:], "\n")

#예제
'''
numberTuple2 = (14, 75, 32, 94)
numberTuple2[0] = numberTuple[0] * 2
튜플은 수정불가능해서 타입에러 발생
'''
