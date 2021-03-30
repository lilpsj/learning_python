# 공공데이터포털 : data.go.kr

''' csv : comma-separated.values
쉼표(,)로 구분한 텍스트 데이터
확장자는 .csv이며 MIME형식은 text/csv이다.
'''

# 비슷한 포맷으로는 탭으로 구분하는 'tab=separated values(TSV)가 있음
# 파일의 확장자와 실제 파일의 내용과는 무관 (예; .jpg => 로 끝난다고 무조건 이미지 파일이 아님)
'''
with open ("C:/Users/ITPS/Desktop/covid.csv", "r") as file:
    #변수 저장 안하는 이유 ; 필요한 데이터가 아닌 데이터 기준이 출력되서
    file.readline()
    
    contents = file.readline()

    #contests에 들어있는 데이터를 ","기준으로 쪼개서 dataList변수에 저장해라
    dataList = contents.split(",")
    
    while True:
        contents = file.readline()
        if contents == "":
            break
        dataList = contents.split(",")
        print(dataList)
'''
# 쪼개진 각각의 데이터 인덱스에 접근하기
# 예제 covid.csv 파일의 데이터를 읽어서, 월별 검사진행자의 수를 구하라
# 월별 진행자 수를 구하기 위해서는 일별 검사진행자의 합계를 먼저 구하기

with open ("C:/Users/ITPS/Desktop/covid.csv", "r") as file:
    file.readline()

    # 월별 검사 진행자의 수
    add = 0
    # 10월달 검사 진행자의 수
    month10_add = 0
    # 11월달 검사 진행자의 수
    month11_add = 0
    # 12월달 검사 진행자의 수
    month12_add = 0

    while True:
        contents = file.readline()
        if contents == "":
            break
        dataList = contents.split(",")
        dataInfo = dataList[0].split("-")

        if dataInfo[1] == '10':
            month10_add = month10_add + int(dataList[3])
        elif dataInfo[1] == '11':
            month11_add = month11_add + int(dataList[3])
        elif dataInfo[1] == '12':
            month12_add = month12_add + int(dataList[3])

        add += int(dataList[3])

    print("전체 검사 진행자의 수 = ", add)
    print("10월 검사 진행자의 수 = ", month10_add)
    print("11월 검사 진행자의 수 = ", month11_add)
    print("12월 검사 진행자의 수 = ", month12_add)

