'''set(집합)
파이썬 2.3부터 추가된 데이터 타입
리스트, 튜플과 마찬가지로 데이터들을 저장할 수 있는 데이터타입
한글 그대로 집합과 관련된 부분을 쉽게 처리하기 위해 만들어진 데이터 타입
-원소의 순서는 고려사항이 아니다
-원소는 중복될 수 없음
-공집합이 있다
변수명 = {값1, 값2, 값3}  <----->  dic 변수명 = {key:value, key:value ...}
변수명 = set(시퀀스객체)
set은 인덱스 번호가 없으므로 인덱스 번호로 데이터에 접근, 슬라이싱 불가능 -> list화, Tuple화 시켜서 사용
'''
numberSet = {1, 2, 3}
stringSet = {"파", "이", "썬"}

print(numberSet)
print(stringSet, "\n")

numberSet1 = {1, 2, 1, 3}
stringSet1 = {"파", "이", "이", "썬"}
print(numberSet1)
print(stringSet1, "\n")
#중복된 데이터는 빠져서 출력됨

emptySet = {}
print("emptySet : ",emptySet)
print("numberSet : ", type(numberSet))
print("emptySet_Type : ", type(emptySet), "\n")
#Type출력시 set이라고 표기되지 않음

emptySet1 = set()
numberSet2 = set([1, 2, 3])
StringSet = set("파이썬")

emptySet2 = list(emptySet1)
numberTuple = tuple(numberSet)
print("set으로 만든 emptySet1 : ", emptySet1)
print("numberSet2를 numberTuple로 : ", type(numberTuple), "\n")

#set교집합 ; & 또는 intersaction 가능
leftSet = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
rightSet = set([2, 4, 6, 8, 10, 12, 14, 16])

print("set교집합1 : ",leftSet & rightSet)
print("set교집합1 : ",leftSet.intersection(rightSet))

#set합집합 ; | 또는 union
print("set합집합1 : ",leftSet | rightSet)
print("set합집합2 : ",leftSet.union(rightSet))

#set차집합 ; - 또는 difference 기능
print("set차집합1 : ",leftSet - rightSet)
print("set차집합2 : ",leftSet.difference(rightSet), "\n")

#set 추가
numberSet3 = {1, 2, 3}
numberSet3.add(4)
numberSet3.add(7)

#set 삭제
numberSet3.remove(7)
'리스트, 튜플 : 인덱스 지정'
'set : 삭제할 데이터를 직접 지정'

#예제
leftSet1 =set(["나는 오늘도 파이썬을 공부한다"])
rightSet1 = set(["나는 내일도 파이썬을 공부한다"])

print("set교집합 : ", leftSet1 & rightSet1)
print("set합집합 : ", leftSet1 | rightSet1)
print("set차집합 : ", leftSet1 - rightSet1)
print("리스트화 : ",type(list(leftSet1)))



