'''
시퀀스 자료형 종류
-시퀀스 자료형의 덧셈 연산은 같은 자료형끼리만 할 수 있다
1. str
2. list
3. tupel
4. range :
   (+) 연산자로 객체를 연결할 수 없다 -> 다른 종류의 시퀀스 자료형으로 변환필요
   (*) 연산자로 객체반복 불가능 -> 다른 종류의 시퀀스 자료형으로 변환필요
   인덱스, 슬라이싱 가능
   특정한 패턴으로 연속되는 수자를 요소로 갖고 있는 시퀀스 자료형
   변수명 =range(시작값(이상), 마지막값(미만), 패턴)

5. byte
6. bytearray
'''

#자료형 변경
simpleString = "문자열"
simpleList = ["리", "스", "트"]
simpleTuple = ("튜", "플")

strToList = list(simpleString)
listToTuple = tuple(simpleList)
tupletoStr = str(simpleTuple)

print("str -> list = ", strToList)
print("list -> tuple = ", listToTuple)
print("tuple -> str = ", tupletoStr, "\n")

#len
print(len(simpleString))
print(len(simpleList))
print(len(simpleTuple), "\n")

#Range
oddRange = range(1, 10, 2)
evenRange = range(2, 10, 2)

print(oddRange)
print(evenRange)
"출력안됌, 리스트로 변경필요"

#Range -> list
rangeToList1 = list(oddRange)
rangeToList2 = list(evenRange)

print("range -> list = ", rangeToList1)
print("list -> range = ", rangeToList2, "\n")

#예제1_1부터 10까지 모든수를 갖고 있는 Range
num_ex1 = range(1,11, )
rangeToList3 = list(num_ex1)
print("예제1 = ", rangeToList3)

#예제2_10부터 1까지 모든수를 갖고 있는 Range
num_ex2 = range(10, 0, -1)
rangeToList4 = list(num_ex2)
print("예제2 = ", rangeToList4, "\n")

#
simpleText = "apple, banana, pineapple"
print("apple" in simpleText)
print("grape" in simpleText)

print("apple" not in simpleText)
print("grape" not in simpleText)

#수정 가능한 데이터 타입
# =읽고 쓸 수 있는 데이터 타입
# =mutable 데이터 타입
# list, set, dic

#수정 불가능한 데이터 타입
# =읽기만 가능한 데이터 타입
# =immutable 데이터 타입
# 정수, 실수, 문자열, 튜플

'''
simpleString = "문자열"
simpleList = ["리", "스", "트"]
simpleTuple = ("튜", "플")

simpleString[0] = "1" -> Type Error
simpleList[0] = 1
simpleTuple[0] =1  -> Type Error
'''






