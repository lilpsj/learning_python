# 테스트 주도 개발 방법론(TTD)
'과정보다 결과를 먼저 도출하고 그 후 결과를 얻기 위한 과정을 만드는 법'

#변수 대신 클래스를 사용하는 이유 => 연관있는 데이터를 묶어주는 것

class Cart:
    # def __init__(self):
     def __init__(self, x, y, speed, frame, goodList):
     # groceries Cart()인스턴스를 만들때, 원하는 값을 가지고 만들 수 있도록 매개변수를 만든것
     # line 41이 해당 인스턴스
         #self.x = 0
          self.x = x
         #self.y = 0
          self.y = y
          self.speed = speed
          self.frame = frame
          self.goodsList = goodList

     def move(self, x, y, speed):
          if (x > 0):
               movedX = x * speed
               print("카트를 x축으로 {0}의 속도로 {1}만큼 움직임".format(speed, movedX))
               self.nowPosition["x"] += movedX

          if (y > 0):
               movedY = y * speed
               print("카트를 y축으로 {0}의 속도로 {1}만큼 움직임".format(speed, movedY))
               self.nowPosition["y"] += movedY

     def putIn(self, goods):
          self.goodsList.append(goods)
          print("카트에 {}을 담았습니다".format(goods))

     def putOut(self, goods):
          self.goodsList.remove(goods)
          print("카트에 {}을 뺐습니다.".format(goods))

     #카트 안 요소를 클래스 내에 출력하기 위한 함수
     def printElement(self):
          print(self.x)
          print(self.y)
          print(self.speed)
          print(self.frame)
          print(self.goodsList)

groceriesCart = Cart(100, 200, 1, "철제", 4)
groceriesCart = printElement()



'''
groceriesCart.move(10, 10, 1)

groceriesCart.putIn("양파")
groceriesCart.putIn("무")
groceriesCart.putIn("마늘")

groceriesCart.putOut("무")

print("담긴 목록 :", groceriesCart.goodsList)
'''