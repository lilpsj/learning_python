#반복문 - continue
'''
-break 문과 마찬가지로
-반복문의 안에서 흐름을 조절할 때 사용
-특정 코드 뭉치들을 실행하지 않고 다시 조건을 비교하고자 할 때
'''

#1~100사이의 수 중 홀수만 출력
'''
i = 1

add = 0

while i <= 100:
    if i % 2 == 1:
    add = add + i

    i = i + 1
'''

i = 1

add = 0

while i <= 100:
    i = i + 1

    if i % 2 == 0:
        continue

    add = add + 1


#예제1
print("입력 : ", end = "")
num = int(input())

if num == 0:
    print("프로그램 종료")
elif num > 0:
    while num >= 1:
        if num % 3 != 0:
            print(num)

    num -= 1
elif num < 0:
    while num <= 1:
        if num % 3 != 0:
            print(num)

        num += 1

#예제2
# 예제2 0~73 중 3으로 끝나는 숫자만
# 3 13 23 33 43 53 63 73
i = 0
while i <= 73 == 3:
    print(i)

    i += 1
