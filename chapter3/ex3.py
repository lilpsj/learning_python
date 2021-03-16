# format 매서드
# 메서드 -> input, print와 같은 기능을 의미

data = "Breakfast is {} and {}". format("spam", "eggs")
#str만 메서드 기능 제공
print(data)

print("My name is {}". format ("Lily"))

print("My name is {0} and {1}". format("Lily", 25))
print("My name is {1} and {0}". format("Lily", 25))

print("=== ===")
print("My name is", "James", "and", 25)
print("My name is %s and %x" % ("James", 25))
print("My name is {} and {}". format("James", 25))

# f-string
# 파이썬 3.6 이후로 나온 새로운 기술
# format 매서드와 비슷하지만
# format 매서드 보다 코드 가독성을 더 높일 수 있음

who = "you"
how = "happy"
f"{who} make me {how}"
print(f"{who} make me {how}")

age = 25
print(f"내년엔 {age+1}살이 됩니다.")