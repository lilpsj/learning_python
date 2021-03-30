'딕셔너리'
#사전이란 뜻처럼 사전과도 같은 역할을 한다.
#변수명 = {key1: value1, key2: value2, ...)
#키는 중복될 수 없으며 값은 중복될 수 있다
#키와 값의 쌍이므로 키는 무작위 순서로 들어간다

''' 
0 - 이름
1 - 생년월일
2 - 주소
3 - 연락처
'''

personInfo = ["이철수",
              "1990년 3월 18일",
              "부산 진구 중앙대로 668",
              "010-1234-5678"
              ]

dic = {"apple": "사과", "banana": "바나나", "pineapple": "파인애플"}

personinfo = {"name" : "이철수",
              "birth" : "1990년 3월 18일",
              "address" : "부산 부산진구 중앙대로 668",
              "tel" : "010-1234-5678"}
print(personinfo)

#딕셔너리 인덱싱
name =  personinfo["name"]
print(name, "\n")

#dic-인덱싱 예제
menu = {"카페 아메리카노" : "4,600원",
        "카페 라떼" : "5,100원",
        "카푸치노" : "5,100d원",
        "오트밀라떼" : "5,400원"}

americano = menu["카페 아메리카노"]
print("아메리카노 = ", americano, "\n")

#dic 키와 값, 목록 찾기
keys = menu.keys()
print(keys)

values = menu.values()
print(values)

items = menu.items()
print(items)

#딕셔너리 추가
menu["돌체라떼"] = 6100
menu.setdefault("espresso", 4100)

'카멜표기법 : 단어와 단어사이에 대문자로 표기'

#딕셔너리 수정
menu["카푸치노"] = 5300
menu.update(돌체라떼 = 6500)
print(menu)
'''update를 사용해서 없는 key에다가 저장하면 코드 가독성이 떨어짐'''

menu["아메리카노"] = 4700
menu["카패 라떼"] = 5100
menu["카푸치노"] = 5300
menu["오트밀라떼"] = 5400
menu["돌체라떼"] = 6500
menu.update(에스프레소 = 4100)
menu.update(더블샷 = 4500)

#딕셔너리 삭제
'처리과정 ; 기존데이터(menu)에서, "오트밀라뗴"를 꺼냄'
removeItem = menu.pop("오트밀라떼")
print(removeItem)

removeItem1 = menu.pop("더블샷")
print(removeItem1)
print(menu)










