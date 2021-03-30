# 외장함수, 파일입출력
# 스트림 : 데이터가 흐르는 / 흘러들어오는 방향
# 스트림의 방향은 one-way
# 출력 스트림 - 데이터가 프로그램에서 바깥으로 나가는 스트림
# 입력 스트림 - 데이터가 바깥에서 프로그램으로 들어오는 스트림

'입/출력 스트림을 파일로 향하게 하기 위해서 -> open이라는 함수 사용'
# 프로그램과 파일을 입력 스트림으로 연결할 수 있고
# 프로그램과 파일을 출력 스트림으로 연결할 수 있다.

'''
변수명 = open("파일의 경로", "파일 모드")

파일모드
입력스트림 : r - 읽기모드 (파일의 내용을 읽을 수만 있음)
출력스트림 : w - 쓰기모드 (파일의 내용을 쓸 수 있음)
출력스트림 : a - 추가모드 (파일의 마지막에 새로운 내용을 추가할 때 사용), append
'''

# 입력장치 : 키보드, 마우스, 카메라, 마이크, 파일
# 입력스트림을 사용해서 연결 - open("파일의 경로", "r")
# 파일(입력장치)에 있는 데이터를 <프로그램에서 사용>하겠다

# 출력장치 : 모니터, 스피커, 프린터, 파일
# 출력스트림을 사용해서 연결 - open("파일의 경로", "w")
# 파일(출력장치)에 있는 데이터를 <파일에 저장>하겠다

"출력스트림 사용"
# 윈도우 체제 파일경로 => /로 변경해주기
file = open("C:/Users/ITPS/Desktop/test.txt", "w")
file.write("Hello World~!")
file.close()
# 스트림을 열었으면 닫아줘야댐
# 닫아주지 않으면 변경사항이 저장이 안됌


"입력스트림 사용"
file = open("C:/Users/ITPS/Desktop/test.txt", "r")
contents = file.readline()
# 입력스트림(r)를 썻을때, write메서드 사용할 수 없음
print(contents, "\n")
file.close()
"실수로 다른 데이터가 들어있는 파일을 w로 오픈할 시 새로운 파일이 생성되는 거라서 기존 데이터 분실위험이 있음"


# 예제 - 1~10번째 줄입니다. 파일에 저장하고 출력하기
file = open("C:/Users/ITPS/Desktop/test.txt", "w")
for i in range(1, 11):
    file.write("%d번째 줄입니다. \n" % i)
file.close()

file = open("C:/Users/ITPS/Desktop/test.txt", "r")
for i in range(1, 11):
    contents = file.readline()
    print(contents, end="")
file.close()
print()


# a모드 - 11 ~ 20번째 줄입니다. 까지 내용을 덧붙이세요.
file = open("C:/Users/ITPS/Desktop/test.txt", "a")
for i in range(11, 21):
    file.write("%d번째 줄입니다. \n" % i)

# 파일에 있는 모든 데이터를 불러올때
file = open("C:/Users/ITPS/Desktop/test.txt", "r")
for i in range(1, 21):
    contents = file.readline()
    print(contents, end="")
file.close()

# with - as : 경로에 있는 파일을  file이라는 변수에 저장
with open("C:/Users/ITPS/Desktop/test.txt", "r") as file:
    contents = file.readlines()
    # readlines => 여러줄의 데이터를 읽어와서 '리스트'에 저장
    # 램용량을 너무 잡아먹어서 잘 안씀, 테스트용으로 사용

    # 파일에 있는 모든 데이터를 불러올때 : for문
    for text in contents:
        # contests안의 리스트들의 text안에 할당
        print(contents)
file.close()

# 파일에 있는 모든 데이터를 불러올때 : while문
'''
    while True:
        contents = file.readline()

        if contents == "":
            break
        else:
            print(contents, end="")
        '''
