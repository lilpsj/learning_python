class Animal:
    def __int__(self, name):
        self.__name = name

    def getName(self):
        """
        비공개 멤버 변수인 name의 값이
        :return:
        """
        return self.__name

    def run(self):
        print(self.__name + "이(가) 네발로 달립니다.")

    def setName(self, name):
        """

        :param name:
        :return: 없음
        """
        self.__name = name

class Rabbit(Animal):
    def __init__(self,name):
        super().setName(name)

class Person(Animal):
    def __init__(self,name):
        super().setName(name)

    def runPerson(self):
        print("사람이 달립니다")

rabbit = Rabbit("토끼")
# rabbit.name = Rabbit()
'class Animal의 인스턴스 메서드에서 "name"은 비공개 변수로 설정되어있기 때문에, 클래스 외부에서 인스턴스 변수로 사용할 수 없다.'
rabbit.run()

person = Person("사람")
person.runPerson()
