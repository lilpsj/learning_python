"""
비트연산자
1. 이진수를 알아야하고
2. 컴퓨터에서 이진수가 어떻게 다뤄지는지 이해하고 있어야하고
3. 우리가 쓰는 10진수 정수를 이진수로 변환할 수 있어야하고
4. 이진수를 다시 10진수 정수로 변환할 수 있어야한다.

-포토샵 같은 이미지 처리프로그램
-프리미어 프로 같은 동영상 편집 프로그램
-알집 같은 압축 프로그램
-V3같은 보안 프로그램

정보처리 기능사 필기 - 불대수 PART
1. & (And)
2. | (Or)
3. ^ (Xor)
4. ~ (Not)
5.<<(Leftshift)
6.>>(Rightshift)
"""

value1 = 10
value2 = 5

bitAndResult = value1 & value2
bitOrResult = value1 | value2
bitXorResult = value1 ^ value2
notResult = ~value1
leftShiftResult = value1 << 2
RightShiftResult = value1 >> 2

print("bitAndResult = ", bitAndResult)
print("bit0rReuslt = ", bitOrResult)
print("bitXorResult = ", bitXorResult)
print("notResult = ", notResult)
print("leftShiftResult = ", leftShiftResult)
print("RightShiftResult = ", RightShiftResult, "\n")




