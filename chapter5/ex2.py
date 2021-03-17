#예제-문자열 덧셈
text1 = "Life is too short,"
text2 = "You need Python"

fullText = text1 + text2
print(fullText, "\n")

'''
            RAM
   주소       |        값
   #1                "안녕"
   #2                "하세요"
   #3               "안녕하세요"
'''

#예제
text1_1 = "어제는 비가 내려"
text1_2 = "시원했습니다"
fullText = text1_1 + text1_2
print(fullText)

text2_1 = "지금은 문자열에 대해서 "
text2_2 = "배우고 있습니다"
fullText = text2_1 + text2_2
print(fullText, "\n")

text3 = "안녕\n"
text4 = "하세요"
print(text3)
print(text4)

fullText = text3 + text4
print(fullText, "\n")

#예제
monja1 = '지금은 "문자"를 변수에 '
monja2 = '저장하는 방법을 배우고 있습니다.'
fullText = monja1 + monja2
print(fullText)

monja3 = '''"문자"는 홑따옴표(')와 '''
monja4 = """ 쌍따옴표(")를 사용해서 저장할 수 있습니다."""
fullText = monja3 + monja4
print(fullText)
