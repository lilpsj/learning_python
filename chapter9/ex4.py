# 클래스 멤버변수와 인스터스 멤버변수의 종류
'동일명의 클래스 속성과 인스턴스 속성이 존재할 수 있음, 그러나 처리 순서가 다름'

'''
클래스 멤버 변수       |       인스턴스 멤버 변수
공개 멤버 변수         |       비공개 멤버 변수

클래스 밖에서 객체명을 이용해서 접근할 수 있는 멤버 변수 = 공개 멤버 변수(kind)
*변수의 이름 앞에 별도의 기호가 없다.

클래스 밖에서 객체명을 이용해서 접근 할 수 없게 만드는 것 = 비공개 멤버변수
*변수의 이름 앞에 __를 붙인다

'''


# 이동 수단의 요소와 기능을 갖는 클래스
class Transport:
    # transport 클래스 안 모든 요소가 passengerList를 공유함
    passengerList = []

    def __init__(self):
        # 이용 요금은 1350원
        self.__charge = 1350
        self.passengerList = []
        # 이동 수단의 종류
        self.kind = ""
        # 이동 수단의 바퀴 개수
        self.wheel = 0
        # 이동 수단 최대 탑승 인원
        self.maximumPeople = 0
        # 이동 수단의 x 위치
        self.x = 0
        # 이동 수단의 y 위치
        self.y = 0

    def move (self, x, y, speed):
        if (x > 0):
            movedX = x * speed

        if (y > 0):
            movedY = y * speed
    def getIn(self, name, fee):
        print("이용 요금은 ", self.__charge, "원 입니다.")
        print("지불하신 금액은 ", fee, "원 입니다.")

        money = fee - self.__charge
        if money > 0:
            print("잔액 ", money, "원 입니다.")
        else:
            print("잔액이 반환되지 않습니다.")

        self.passengerList.append(name)
       #Transport.passengerList.append(name)
    # 인스턴트 요소에 passengerList가 없기 때문에 연산을 줄이기위해
    # 클래스 요소로 바로 접근 가능하도록 코드를
    # Transport.passengerList.append(name)이라고 변경해주기

bicycle = Transport()
bicycle.getIn("홍길동", 1500)
bicycle.__charge = 1500

vehicle = Transport()
vehicle.getIn("설까치")

motorcycle = Transport()
motorcycle.getIn("하니")

print(bicycle.passengerList)
print(vehicle.passengerList)
print(motorcycle.passengerList)
print(Transport.passengerList)

'''
['홍길동', '설까치', '하니']
['홍길동', '설까치', '하니']
['홍길동', '설까치', '하니']로 출력됨

1.bicycle의 인스턴스 요소에 passengerList가 있는지?
2. yes => 
3. no => Transport 클래스 요소에 passengerList가 있는지?
4. yes =
'''