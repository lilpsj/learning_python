'''if 조건문
프로그램의 흐름을 만들 수 있는 첫 단계
특정 소스를 만족할 때 소스코드들을 실행

코드 블록 : 여러 소스 코드를 한덩어리로 뭉침
일반적인 프로그래밍 언어 - {}
파이썬 - 들여쓰기(tab), 내어쓰기(shift+tab)

1. if
2. if else
3. if elif (if else if)
4. if elif else (if else if else)
'''

if True :
    print("조건식이 참이므로")
    print("소스코드가 실행됩니다")

if False :
    print("조건식이 거짓이므로")
    print("소스코드가 실행되지 않습니다")

print("프로그램 종료", "\n")


#예제1 - 미세먼지 농도는 0부터 10까지, 미세먼지 농도 5이상이라면 마스크를 쓰고 나간다
print("오늘의 미세먼지 농도를 입력하세요")
findust = input()
findust =int(findust)
if findust >= 5:
    print("마스크를 쓰세요", "\n")

#예제2 만원 이상이면 택시를 탄다
taxifee = int(input())
if taxifee >= 10000:
    print("택시를 탄다", "\n")

#예제3 비가 오면 우비를 입고 나간다
print("비가 오나요? 온다면1, 오지 않는다면 0을 입력하세요")
isRaining = int(input())

if isRaining == 1:
    print("우비를 입고 나가세요", "\n")
"True = 0이 아닌 값 / False = 0일 떄 사용할 수 있음"

#예제4 입력받은 수가 홀수면 홀수를 출력
print("수 : ", end="")
num = int(input())
if num % 2 != 0:
    print("홀수")

#예제5 입력받은 수가 짝수면 짝수, 홀수면 홀수 출력
print("수 : ", end="")
num1 = int(input())
if num1 % 2 != 0:
    print("홀수")

if num1 % 2 == 0:
    print("짝수")
