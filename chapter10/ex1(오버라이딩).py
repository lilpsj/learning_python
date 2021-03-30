class A:
    def print(self):
        print("A")

class B(A):
    pass

class C(B):
    def print(self):
        print("C")

'오버라이딩'
# 상속 관계에서 부모클래스로부터 물려받은 메서드를
# 자식 클래스에게 맞게 구현을 바꾸는 것
# 자식 클래스가 오버라이딩을 하려면 부모 클래스의 메서드 정의(def) 부분은 똑같이, 구현(print)만 다르게 해야함

a = A()
b = B()
c = C()

a.print()
b.print()
c.print()
