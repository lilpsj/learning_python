'반지름을 입력받아 원의 넓이를 반화하는 get_area()함수'
'7.06858334705770345'

import math

def get_area(radius):
    """
    :param radius: 반지름
    :return: 원의 넓이
    """
    area = math.pi*math.pow(radius, 2)
    return area

radius = 1.5
area = get_area(radius)
print(area)
print(get_area.__doc__)


'p49-1'
student = '31025'
grade_no = student[0]
class_no = student[1:3]
stu_no = student[3:]
print(f"{grade_no}학년, {class_no}반, {stu_no}번, \n")

# 31025 -> str로전환해야 인덱싱가능

'p49-2'
car1 = "서울2가1234"
car2 = "10가1234"
car3 = "288가1234"

car1_no = car1[-4:]
car2_no = car2[-4:]
car3_no = car3[-4:]

print(f"{car1}의 차량번호 4자리는 {car1_no}입니다")
print(f"{car2}의 차량번호 4자리는 {car2_no}입니다")
print(f"{car3}의 차량번호 4자리는 {car3_no}입니다 \n")

'p49-3'
s = "maple"
print(len(s)//2)

