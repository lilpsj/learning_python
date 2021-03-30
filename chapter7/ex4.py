# 두 수와 산술 연산자 중 한 연산자를 전달받아
# 두 수를 사용자가 원하는 산술 연산한 결과를 반환하는 함수

'입력 : 두수, 산술 연산자'
'리턴 : 산술 결과'

def calculator(var1, var2, var3):
    if var3 == "+":
        return var1 + var2
    elif var3 == "-":
        return var1 - var2
    elif var3 == "*":
        return var1 * var3
    elif var3 == "/":
        return var1 / var2


print("첫 번째 수 : ")
num1 = int(input())

print("두 번째 수 : ")
num2 = int(input())

print("연산자 (+, -, *, / ) : ")
var3 = input()

result = calculator(num1, num2, var3)
print("첫 번째 수와 두 번 째 수의 연산결과는", result, "입니다")
print()

# 하나의 return만 사용해서
# 사용자가 원하는 연산 결과를 반환
def calc(var4, var5, op):
    result1 = 0

    if op == "+":
        result1 = var4 + var5
    elif op == "-":
        result1 = var4 - var5
    elif op == "*":
        result1 = var4 * var5
    elif op == "/":
        result1 = var4 / var5
    else:
        print("연산자를 잘못입력하셨습니다")
        return result1

print("첫 번째 수 : ")
num4 = int(input())

print("두 번째 수 : ")
num5 = int(input())

print("연산자 (+, -, *, / ) : ")
var6 = input()

result1 = calc(num4, num5, var6)
print("첫 번째 수와 두 번 째 수의 연산결과는", result1, "입니다")