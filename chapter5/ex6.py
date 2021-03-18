'''
리스트
숫자, 문자열과 같은 데이터의 한 종류
변수명 = [데이터1,  데이터2, 데이터3, ..]
리스트 내 데이터들을 요소라고 부름
리스트 내 요소의 순서가 있고 데이터의 중복을 허용

emptyList = []

numberList = []

floatNumberList = [3.14, 0.14, 0.34]

duplicateNumber = [1, 1, 1]

stringList = ["나는", "지금"]

variousList = [1, "파이썬을", 2, "공부하고 있다"]

complexList = ([1,2], 3, ["파", "이", "썬"])
'''

#리스트 연산 - 덧셈
oddList = [1,3,5,7,9]
evenList = [2,4,6,8,10]

fullList = oddList + evenList
print(fullList, "\n")


#예제1
stringList_1 = ["나는", "지금"]
stringList_2 = ["파이썬을", "공부하고 있다"]
fullstringList = stringList_1 + stringList_2

print("예제1 = ", fullstringList)

#예제2
numberList_1 = [1,2,3]
numberList_2 = [4,5,6]
fullNumberList = numberList_1 + numberList_2

print("예제1 = ". fullNumberList, "\n")

#리스트 연산 - 곱셈
dumyList = [1] * 5
print(dumyList)

stringList_1 = ["나는", "지금"] * 2
print(stringList_1)

numberList_1 = [1,2,3] * 3
print(numberList_1)

#리스트 인덱싱
'''
numberList_5 = [14, 75, 32, 94]
print(numberList_5[0])
print(numberList_5[1])
print(numberList_5[2])
print(numberList_5[3])
'''

#리스트 슬라이싱
nuberList_6 = [14, 75, 32, 94]
print(nuberList_6[1:3])
print(nuberList_6[:3])
print(nuberList_6[1:])
print(nuberList_6[:3])

#리스트 수정
numberlist1 = [14, 75, 32, 94]
numberlist1[0] = numberlist1[0] * 2
numberlist1[1] = numberlist1[1] * 2
numberlist1[2] = numberlist1[2] * 2
numberlist1[3] = numberlist1[3] * 2

'''
리스트는 요소를 추가 또는 삭제할 수 있다.
- 요소 추가 : append, insert
- 요소 삭제 : pop
'''

#4명의 시험성적
numberlist = [14, 75, 32, 94]

#전학온 학생의 성적 추가
numberlist.append(77)
"nuberList가, append메서드를 써서, 77을 추가"

#특정 인텍스에 데이터를 저장
numberlist8 = [14, 75, 32, 94]
numberlist8.insert(0, 59)
print(numberlist8)
"numberlist에, insert메서드를 써서, 0번 리스트 사이에, 59를 추가"

deleteNumber = numberlist8.pop(1)
print("삭제할 데이터는 %d" % deleteNumber)
print(numberlist8)

#특정 인덱스의 데이터를 제거
numberlist8.pop(0)
print(numberlist8)

'''
append 메서드 또는 pop메서드를 인덱스 번호 없이 사용할 때는 조심할 부분이 없음
(리스트의 맨 뒤에 데이터를 추가하거나 삭제하는 동작)

insert 메서드 또는 pop메서드를 인덱스 번호 있이 사용할 때는 조심해야함
(리스트의 중간 또는 맨 앞에 데이터를 추가하거나 삭제하는 동작)
'''