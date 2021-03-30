'''
클래스 바깥에 기능이 정의되어 있으면 : 함수
클래스 안에 기능이 정의되어 있으면 - 메서드
메서드의 첫번째 매개변수는 반드시 필요하다
메서드의 첫번째 매개변수 이름은 self를 사용한다
매개변수가 필요하지 않은 메서드라도 반드시 첫번째 매개변수인 self를 넣어줘야한다

          RAM
#1         | Character
#2 warrior | #1 메모리주소
#3         | Character
#4 archer  | #3 메모리주소

#2 warrior 객체는 #1 메모리주소를 따라 Character클래스로 들어감
Charactoer 클래스에 있는 생성자 HP = 0으로 만듬
(반복) MP = 0, 마법공격력 = 0, 물리공격력은 = 0
warrior 객체에 저장된  MP = 100, HP = 50, 마법공격력은 = 10, 물리공격력은 = 5로 순서대로 처리

#4 archer도 동일한 순서로 처리
'''

class Character:
    # 클래스는 속성을 갖고 있고
    # 캐릭터를 예로 들면, 속성 = 그 캐릭터를 위한 능력치
    # HP, MP, 물리공격력, 마법공격력

    # __init__ 라는 메서드(=생성자)를 정의하고
    # 생성자 안에 클래스가 필요한 속성들을 정의한다
    # 생성자 메서드는 우리가 호출할 수 없는 메서드
    # 일반적인 attack과도 같은 메서드는 우리가 호출할 수 있는 메서드

    def __init__(self):
        self.HP = 0
        self.MP = 0
        self.마법공격력 = 0
        self.물리공격력 = 0


    # 클래스는 기능을 갖고 있다.
    # 캐릭터로 예로 들면, 기능 - 공격, 이동, 대화하기, 길드 가입하기,...
    def attack(self, target):
        # def attack(self, monsterHP, warrior물리공격력)
        # 에서 warrior물리공격력은 def attack함수가 class안으로 들어갔기 때문에 제거

        print("attack 함수 안")
        # 공격을 하기 위한 모션(그래픽처리)

        target.HP = target.HP - self.물리공격력
        '''
        target.HP = archer의 능력치가 저장된 메모리 주소를 가리킴
        70 - 10 = target.HP 변수에 저장됨
        archer객체가 전달된 것이기 때문에 결과값 60이 archer 객체 메모리 주소 안에 저장됨
        따라서 리턴이 필요가 없음
        '''
        # 공격을 받은 후 모션(그래픽처리)

    def say(self):
        pass

    def buy(self):
        pass

    def exit(self):
        pass

# warrior 객체
warrior = Character()
warrior.HP = 100
warrior.MP = 50
warrior.물리공격력 = 10
warrior.마법공격력 = 5

# archer 객체
archer = Character()
archer.HP = 70
archer.MP = 70
archer.물리공격력 = 7
archer.마법공격력 = 7

archer.HP = warrior.attack(archer)
print(archer.HP)

warrior.HP = archer.attack(warrior)
print(warrior.HP)

'''
매개변수에 (archer or  warrior)객체를 전달했을 때는 더이상 return을 하지 않아도 됌
왜? archer는  archer객체의 능력치가 저장된 메모리 주소 그 자체이기 때문에
'''


'line77부터 처리순서'
# arher.HP = 70이라는 숫자를 복사해서 def attack 함수 올라가서 monsterHP 매개변수로 내려옴
# line48에 와서 monsterHP에 복사된 70이 들어감
# monsterHP 변수에 70 - self.물리공격력 10으로 60이 저장됨
# monsterHP 변수에 저장된 결과값 60을 가지고 return됨
# monsterHP 변수에 저장된 값은 = 공격대상의 HP
# 따라서 line79 코드가 만들어질 수 있음


'''
# chapter9.ex2 위한 코드-------------------------------------------------------------------------------------------------
def attack(self, monsterHP, warrior물리공격력):
    print("attack 함수 안")
    # 공격을 하기 위한 모션(그래픽처리)

    monsterHP = monsterHP - warrior.물리공격력

    # 공격을 받은 후 모션(그래픽처리)

    return monsterHP


warriorHP = 100
warriorMP = 50
warrior물리공격력 = 15.7
warrior마법공격력 = 5


archerHP = 75
archerMP = 75
archer물리공격력 = 17
archer마법공격력 = 10
'''