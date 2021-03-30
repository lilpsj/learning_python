' 파일복사 - 원본 파일에 들어있는 데이터를 읽어와서 변수에 저장한 뒤 새로운 파일에 저장하는 것 '
# 데이터의 종류
' 1. 텍스트 데이터 : 문자로 이루어진 데이터 / 주로 사람이 사용하는 데이터'
' 2. 바이너리(이진) 데이터 : 0과 1로만 이루어진 데이터 / 주로 컴퓨터가 사용하는 데이터 / 음악,동영상 이미지 etc'

# r - 입력스트림 연결
# w, a - 출력스트림 연결

# t - 텍스트 데이터를 위한 스트림
# b - 바이너리 데이터를 위한 스트림

# rt - 텍스트 데이터를 위한 입력스트림
# wt, at - 텍스트 데이터를 위한 출력스트림
# rb - 바이너리 데이터를 위한 입력스트림
# wb, ab - 바이너리 데이터를 위한 출력스트림

# 운영체제마다, 프로그래밍 언어마다 줄바꿈 문자가 다름
# 윈도우 - \r\n
# 리눅스 - \n
# 유닉스, MacOS

# 바이너리는 read 메서드 사용해서 읽을 수 있음
'''
with open("C:/Users/ITPS/Desktop/source.mp4", "rb") as source:
    contents = source.read()

with open("C:/Users/ITPS/Desktop/destination.mp4", "wb") as destination:
    destination.write(contents)
'제대로 복사가 됐는지 확인하는 법 : 원본파일과 복사파일 속성에 들어가서 크기 확인'
'''

# 바이너리 파일 복사하기
with open("C:/Users/ITPS/Desktop/source.mp4", "rb") as source:
    print("원본 파일 오픈")
    with open("C:/Users/ITPS/Desktop/destination.mp4", "wb") as destination:
        print("복사 파일 오픈")
        print("복사 시작")
        while True:
            buffer = source.read(1024)

            if not buffer:
                break
            destination.write(buffer)
        print("복사 끝")
    print("원본 파일 스트림 닫음, \n")

# 텍스트 파일 복사하기
with open("C:/Users/ITPS/Desktop/test.txt", "rt") as text:
    with open("C:/Users/ITPS/Desktop/textCopy.txt", "wt") as textCopy:
        while True:
            copyData = text.readline()
            if copyData == '':
                break
            else:
                textCopy.write(copyData)

        print("복사 끝")
    print("원본 파일 스트림 닫음")
            # copyDate = text.read()

            # if not copyData:
                # break
            # textCopy.write(copyData)



