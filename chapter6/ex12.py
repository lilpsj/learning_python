#range 반복문

condition = range(1, 11)

add = 0

for i in condition:
    add = add + i

print(add, "\n")

'''
#예제1 - 구구단 2단
condition1 = range(1, 10)

forward = 2

for backward in range(1, 10):
    result = forward * backward
    print("%d * %d = %d" % (forward, backward, result))
'''


#예제2
#언팩킹 => 튜플에 들어있는 요소를 찢어서 변수에 저장
interviewResult = [
    ("홍길동", "sbs@naver.com", 45),
    ("홍길동1", "sbs@naver.com", 79),
    ("홍길동2", "sbs@naver.com", 85),
    ("홍길동3", "sbs@naver.com", 99),
    ("홍길동4", "sbs@naver.com", 69)
]


for (name, email, point) in interviewResult:
    if point < 80: continue

    print("\n")
    print("발신자 : <SBS아카데미컴퓨터아트학원>")
    print("수신자 : <{0}>". format(email))
    print("내용 : ")
    print("축하드립니다. %s님은 %d점으로 면접에 학습하셨습니다." % (name, point), "\n")

'''
#예제3-구구단 2단부터 5단까지
condition1 = range(1, 10)

forward = 2

for backward in range(1, 10):
    result = forward * backward
    print("%d * %d = %d" % (forward, backward, result))

condition1 = range(1, 10)

forward = 3

for backward in range(1, 10):
    result = forward * backward
    print("%d * %d = %d" % (forward, backward, result))

condition1 = range(1, 10)

forward = 4

for backward in range(1, 10):
    result = forward * backward
    print("%d * %d = %d" % (forward, backward, result))

condition1 = range(1, 10)

forward = 5

for backward in range(1, 10):
    result = forward * backward
    print("%d * %d = %d" % (forward, backward, result))
'''
#중첩 for문 예제
for forward in range(2, 6):
     for backward in range(1, 10):
        result = forward * backward
        print("%d * %d = %d" % (forward, backward, result), "\n")

#예제2
print("줄 수 = ", end="")
line = int(input())
'''내꺼 틀린답
for lineCount in range(1, line+1):
     for stars in range(1, lineCount+1):
         print("*", "\n", end="")
'''
for lineCount in range(1, line+1):
    for stars in range(1, lineCount+1):
        print("*", end="")
    print()

