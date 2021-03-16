'''
비교연산자 - 두 수를 비교할 때 사용
결과 -> bool(논리값)
bool 타입의 데이터 -> True / False
비교 연산의 기준은 왼쪽!

1. == 같다
2. != 다르다
3. > 크다(초과)
4. < 작다(미만)
5. >= 크거나 같다(이상)
6. <= 작거나 같다(이하)
'''

value1 = 10
value2 = 5

eqResult = value1 == value2
neqResult = value1 != value2
gtResult = value1 > value2
ltResult = value1 < value2
gteResult = value1 >= value2
lteResult = value1 <= value2

print("eqResult = ", eqResult)
print("neqResult = ", neqResult)
print("gtResult = ", gtResult)
print("ltResult = ", ltResult)
print("gteResult = ", gteResult)
print("lteResult = ", lteResult)