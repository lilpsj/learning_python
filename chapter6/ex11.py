#반복문 - for
'''
for 변수 in 시퀀스객체:
    코드1
    코드2
    ...

-while문과는 다르게 in의 우변에 있는 값이 in의 좌변에 할당된다.
'''

simpleList = ["one", "two", "three"]

for word in simpleList:
    print(word)


#예제1
'''
1.숫자 2.문자열 3.리스트 4.튜플 5.딕셔너리 6.집합 7.불
김철수 36
고영희 70
홍길동 83
이영수 59
최영길 61
'''
scoreList = [
    {"이름": "김철수", "점수" : 36},
    {"이름": "고영희", "점수": 70},
    {"이름": "홍길동", "점수": 83},
    {"이름": "이영수", "점수": 59},
    {"이름": "최영길", "점수": 61}
]

for score in scoreList:
    if score["점수"] > 60:
        print("%s는 합격" % score["이름"])
    else:
        print("%s는 불합격" % score["이름"])
