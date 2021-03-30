# 사람 클래스를 만드세요
# 사람은 눈, 코, 입, 귀의 개수를 갖고 있고
# 팔, 다리, 손가락, 발가락의 개수를 갖고 있습니다
# 사람은 먹고, 말하고, 자는 동작을 합니다.

# 클래스 생성
class Human:
    # 생성자 호출
    def __init__(self):
        self.name
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1
        self.arm = 2
        self.leg = 2
        self.finger = 10
        self.toe = 10

    def eat(self):
        print(self.name, "이(가) 먹습니다")

    def talk(self):
        print(self.name, "이(가) 말합니다")

    def sleep(self):
        print(self.name, "이(가) 잡니다")

# 객체 생성
# user1 객체 (참조변수)
user1 = Human()
user1.name = "사람1"
user1.eat()
'''
user1.eat() 처리과정
user1.eat멤버변수가 class 인스턴스(self)로 가서
(def eat(self)생성자로 들어감
self.name = user1의 name(="사람1"), "이(가) 먹습니다" 라고 출력
'''