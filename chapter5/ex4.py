'''문자열 인덱싱'''

text = "python is easy"

#인덱스 번호
"p|y|t|h|o|n| |i|s| |e |a |s |y"
"0|1|2|3|4|5|6|7|8|9|10|11|12|13"
"-14|-13|-12|-------------|-2|-1"


print(text[0])
print(text[1], "\n")

text = "Life is too short, You need Python"
print(text[0])
print(text[1], "\n")

monja1 = text[0]
monja2 = text[1]
monja3 = text[10]
#처리과정 ; 0번 자리에 있는 L은 그대로 있고, L이 복사되어서 사용되는것

print(monja1)
print(monja2)
print(monja3, "\n")
#처리과정 ; 가리키는 값을 복사하여 출력하는 것

ex1 = text[6]
ex2 = text[13]
ex3 = text[9]
ex4 = text[15]
ex5 = text[16]
print(ex1)
print(ex2)
print(ex3)
print(ex4)
print(ex5, "\n")

text = "Life is too short, You need Python"
print(text[-1])
print(text[-2])
print(text[-9])

#양수 인덱스 번화와 음수 인덱스 번호를 적절히 사용해서
#아래와 같이 출력하세요

text = "python is easy"
word1 = text[0] + text[1] + text[2] + text[3] + text[4] + text[5]
word2 = text[7] + text[8]
word3 = text[-4] + text[-3] + text[-2] + text[-1]

print((word1) + (word2) + (word3))
