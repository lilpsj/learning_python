# 두 정수 중 최대값을 구하세요.
maximum = max(1,10)
print(maximum, "\n")

numberList = [1, 3, 7, 10, 2, 8, 9]
maximum = max(numberList)
print(maximum)
print("정렬 전")
print(numberList)

# range, list, tuple, len
# sorted 함수 - 정렬 (오름차순)
print("정렬 후")
print(sorted(numberList))

# 오름차순 정렬 함수만들어보기
testList = [2, 1, 3, 5, 4]
'''
if testList[0] > testList[1]:
    temp = testList[1]
    testList[1] = testList[0]
    testList[0] = temp

if testList[1] > testList[2]:
    temp = testList[2]
    testList[2] = testList[1]
    testList[1] = temp

if testList[2] > testList[3]:
    temp = testList[3]
    testList[3] = testList[2]
    testList[2] = temp

if testList[3] > testList[4]:
    temp = testList[4]
    testList[4] = testList[3]
    testList[3] = temp

print(testList)
'''
for i in range(1, 5):
    if testList[i-1] > testList[i]:
        temp = testList[i]
        testList[i] = testList[i-1]
        testList[i-1] = temp
    print(testList)
# 이 반복문의 한계는?
# 데이터가 늘어나면 for i in range(1, x) 횟수를 일일이 세서 바꿔줘야함

'len을 사용해서 수정한 코드'
testList1 = [2, 1, 3, 5, 4, 9, 8, 7, 10]
for i in range(1, len(testList1)):
    if testList1[i-1] > testList1[i]:
        temp = testList1[i]
        testList1[i] = testList1[i-1]
        testList1[i-1] = temp
    print(testList1)
