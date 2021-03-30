'''
while 반복문
-if문과 마찬가지로 조건에는 연산의 결과가 bool자료형이어야 한다.
-조건이 참일 경우에만 실행

i = 0                              i가 0일 때

while i < 100 :                    i가 0부터 100미만일(99까지) 동안
    print("Hello, wolrd!")         Hello, world!를 100번 반복출력

    i += 1                         0부터 하나씩 늘려가면서

i=0
비교(0이 100보다 작은가?)
출력(T = "Hello world)
증가(처음값에서 +1) => 반복

i=1
비교(1이 100보다 작은가?)
출력(T = "Hello world)
증가(처음값에서 +1) => 반복
'''
# 언제 시작하고, 값이 어떻게 증가면서, 언제 종료됐는지 체크 필수"
# 메모장에 i=0적고 확인 -> i=1적고 확인 (반복)
# i +=1이 없어지면? 무한루프 -> "Hello, world!"를 계속 반복해서 출력

n = 1

while n <= 10:
    print(n)

    n += 1
#n=11, n이 10이상 => 프로그램 종료


#예제10
hit = 0

while hit < 10:
    hit = hit + 1
    print("나무를 %d번 찍었습니다" % hit)

    if hit == 10:
        print("나무가 넘어갑니다.")
        print("\n")

# 횟수반복문 = 반복횟수가 정해져있는 반복문
# 반복횟수가 정해져 있는 부분은 while문과는 맞지 않음

'''while문과 어울리는 프로그램
- 특정 조건을 만족할 때까지 주사위를 굴리는 프로그램
- 경품 추첨 이벤트 프로그램
- 로또 당첨 번호 선정 프로그램
'''

#random
'''
import random

#주사위를 한번 굴림
dice = random.randint(1, 6)
print (dice)

dice = random.randint(1, 6)
print (dice)

dice = random.randint(1, 6)
print (dice)
'''

#예제2
# 1~6까지 있는 주사위를 굴려서 4가 나올 때까지 주사위를 굴리는 프로그램
import random

dice = 0
#주사위에는 다른 숫자를 넣을시 4가 아닐때까지 안정적으로 연산이 안될 수 있기 때문에, 절대 나오지 않을 0을 입력

while dice != 4:
#주사위가 4가 아닐 때까지
    dice = random.randint(1, 6)
#6까지 잇는 주사위를 1번 굴려라
    print("dice =  %d" % dice)
#dice = () 출력


