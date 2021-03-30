class PersonFaceInfo:
    def __init__(self, eye, nose, mouth):
        self.eye = eye
        self.nose = nose
        self.mouth = mouth

class PersonBodyInfo:
    def __init__(self, finger, toe, leg):
        self.finger = finger
        self.toe = toe
        self.leg = leg

# 사람은 눈, 코, 잎, 손가락, 발가락, 다리를 갖고 있고
# 숨쉬고, 먹고, 말하기를 할 수 있다.
class Person:
    def __init__(self, eye, nose, mouth, finger, toe, leg):
        # 얼굴과 관련된 데이터
        self.PersonFaceInfo = PersonFaceInfo(eye, nose, mouth)
        # 몸과 관련된 데이터
        self.PersonBodyInfo = PersonBodyInfo(finger, toe, leg)

    # 눈,코,입은 PersonFaceInfo 클래스로 묶이고
    # 손가락, 발가락, 다리는 PersonBodyInfo 클래스로 묶여서
    # eye, nose, mouth 각자의 객체를 출력할 수 없음
    # print(self.eye) -> print(self.PersonFaceInfo.eye)로 수정
    # 완성된 코드를 재수정하는 것 = 코드이펙토링

    def showInfo(self):
        print(self, self.PersonFaceInfo.eye)
        print(self.PersonFaceInfo.nose)
        print(self.PersonFaceInfo.mouth)
        print(self.PersonBodyInfo.finger)
        print(self.PersonBodyInfo.toe)
        print(self.PersonBodyInfo.leg)

    def breath(self):
        print(self, "숨쉬기")

    def eat(self):
        print("먹기")

    def say(self):
        print("말하기")

# 학생은 사람의 특징을 갖고 있으면서 신분이 학생이다
# 학생은 사람의 기능을 하면서 공부도 할 수 있다
class PersonStudent(Person):
    def __init__(self, eye, nose, mouth, finger, toe, leg):
        # 얼굴과 관련된 데이터
        self.PersonFaceInfo = PersonFaceInfo(eye, nose, mouth)
        # 몸과 관련된 데이터
        self.PersonBodyInfo = PersonBodyInfo(finger, toe, leg)

    def study(self):
        print("공부하기")

person1 = Person(2, 1, 1, 10, 10, 2)
person1.showInfo()
person1.breath()
print()

personStudent1 = PersonStudent(2, 1, 1, 10, 10, 2)
personStudent1.breath()

# 클래스 상속 - 공통된 특징을 지니는 클래스들을 만들 때
# 모든 클래스의 최상위 부모 클래스는 Object 클래스임
# class PersonStudent(child) < class Person(parent) < Object(Top Parent)
                              # class Person(Object) <- Objcet
'''
<기반 클래스 ; parent, base, super class>
1. 자신의 요소를 물려주는 클래스 = 부모, 슈퍼 클래스
2. 부모 클래스는 자식 클래스의 멤버변수, 메서드를 사용할 수 없다.

<파생 클래스 ; derived, child, sub class> 
1. 부모 클래스로부터 요소를 물려받는 클래스 = 자식, 자손 클래스
2. 부모 클래스로부터 상속받은 멤버변수와 메서드를 사용할 수 있다.
3. 자식 클래스는 또다른 클래스의 부모변수가 될 수 있다.
예) 생물 > 동물 > 척추동물 > 포유류

다형성 : 한 클래스가 시점에 따라서 상속 받은 부모 클래스가 될 수 있다.

class 클래스이름(상속할 클래스 이름):
    속성
    기능
'''

#