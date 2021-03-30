'''
문자열 슬라이싱
변수명[시작변호:끝번호]
시작번호 <= 문자열번호 < 끝번호
시작번호와 끝번호를 생략할수 있음
'''

text = "python is easy"
#python
print(text[0:6])
print(text[:6])

#is
print(text[7:9])

#easy
print(text[10:14])
print(text[10:],"\n")

text = "Life is too short, You need Python"

#is
print(text[5:7])

#too
print(text[8:11])

#You need Python
print(text[19:])

#Life is too short,
print(text[:19])

#Life is too short, You need Python
print(text[:],"\n")

#인덱스 번호 하나를 지정해서 접근할 때는 인덱스 범위를 벗어나면 컴파일에러 발생
print([text[14])
