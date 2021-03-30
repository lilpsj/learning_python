'충첩 if문'
''' if 조건1 :
        코드1
        코드2
        if 조건2 :
           코드2-1
           코드2-1
        if 조건3 :
            코드3-1
            코드3-2 
'''

#예제1
#성적 0 ~ 100
score = 80
#과제 0 ~ 10
report = 10

#성적이 80점 이상이면서 과제 점수가 10점이면 A+
#성적이 80점 이상이면서 과제점수가 10점이 아니면 A

if score >= 80:
    if report == 10:
        print("예제1 : ", "A+")
    if report != 10:
        print("예제1 : ", "A")

#예제2 비교연산자 사용
score1 = 80
report1 = 9
if score1 >= 80 and report1 == 10:
    print("예제2 : ", "A+")
if score1 >= 80 and report1 != 10:
    print("예제2 : ", "A", "\n")

#예제3
print("미세먼지 농도를 입력하세요 ", end="")
findust = int(input())
if findust >= 5:
    print("마스크를 쓰고 나간다")

    print("가진 현금을 입력하세요 ", end="")
    money = int(input())
    if money >= 10000:
      print("택시를 타세요", "\n")

#예제4
score2 = 40
report2 = 4
if score2 >= 50:
    if report2 >= 5:
        print("Perfect Pass")
    if report2 < 5:
        print("Pass")

if score2 < 50:
    if report2 >= 5:
        print("Fail")
    if report2 < 5:
        print("Perfect Fail")
