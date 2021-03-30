# chapter8/ex3/covid 예제 함수 활용한 코드

with open ("C:/Users/ITPS/Desktop/covid.csv", "r") as file:
    file.readline()
    add = 0
    # 각 월을 변수에 저장하지 않고, 리스트를 활용해서 if문 없이 코드 만들기
    # 월별 검사 진행자의 수
    while True:
        contents = file.readline()
        if contents == "":
            break
        monthAddList = [-1,0,0,0,0,0,0,0,0,0,0,0,0]

        dataList = contents.split(",")
        dataInfo = dataList[0].split("-")

        year = int(dataInfo[0])
        month = int(dataInfo[1])
        day = int(dataInfo[2])

        monthAddList[int(dataInfo[1])] = monthAddList[int(dataInfo[1])] + monthAddList[int(dataInfo[3])]
        add = add + int(dataList[3])

    print("전체 검사 진행자의 수 = ", add)

    for i in range(1, 13):
        print("%d월 검사 진행자의 수 = %d" % (i, monthAddList[1]))
