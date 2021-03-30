# 1 더하기 1을 출력하는 함수
def add0():
    print(1+1)

add0()

# return이 포함된 함수
# 1 + 1의 결과를 반환하는 함수
def add1():
    return 1 + 1
'함수의 끝을 만나면 제어가 8로 돌아가는데, 1+1 결과의 값을 가지고 돌아감'

result = add1()
print(f"add1 함수의 결과값 = {result}")
# return을 만나서 결과값을 가지고 제자리로 들어오니까
# 대입연산을 통해 result라는 변수에 함수를 저장

# 두 수를 더한 결과를 반환하는 함수
def add2(num1, num2):
    return num1 + num2

add2(1, 1)
print(f"add2 함수의 결과값 = {add2(1, 1)}")
'''처리과정
add2(1,1)에 있는 1, 1 인자를 각각 복사해서 함수로 올라감
함수 안으로 들어가서  return 만나서 제자리로 돌아가려는데 결과값을 가지고 가라고 명령되어 있음
결과 값을 가지고 제자리로 돌아옴
출력
'''

# 예제1 - 두 정수 중 큰 수를 반환하는 함수
def maximum(num1, num2):
    max = num1
    if num2 > max:
        max = num2
    return max
    # return = 끝을 의미, 그러나 제어값을 가지고 돌아가는 기능

# 예제2 - 두 정수 중 작은 수를 반환하는 함수
def minimum(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2
'''
 return 출구 2개
 num1 < num2일 때, num1을 가지고 리턴
 num1 > num2일 때, num2를 가지고 리턴
'''

# 예제3 - 세 정수 중 가운데 수를 반환하는 함수
def mid(num1, num2, num3):
    if num1 >= num2:
        if num2 >= num3:
            return num2
        elif num1 <= num3:
            num1
        else:
            return num3
    elif num1 > num3:
        return num1
    elif num2 > num3:
        return num3
    else:
        return num2

# 예제4 -  국, 영, 수 점수를 전달받아/ 합계와 /평균을/ 반환/하는 함수
def calcScore(kor, eng, math):
    sum = kor + eng + math
    avg = sum / 3

    # 합계와 평균을 반환하는 return문
    'return (sum, avg)도 가능 - 리스트로 데이터 저장'
    return {"합계" : sum, "평균" : avg}
'''
    return(sum)
    return(avg)
    라고 안적는 이유는 return(sum)을 만나고 끝이라서 return(avg)실행 안됌
'''

result = calcScore(1, 2, 3)
print(result["합계"])
print(result["평균"])
