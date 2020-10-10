N = input()
sumNum = 0
listNum = list(N)
result = 0
for i in range(1, int(N) + 1):  # 0부터 input값까지 반복
    listNum = []
    listNum = list(str(i))
    #     print("i:", i, ", listNum:", listNum)

    for j in range(len(listNum)):  # 분해합 구하는 식
        temp = int(listNum[j])
        #        print("temp:", temp)
        sumNum += temp

    sumNum += i
    #     print("sumNum:", sumNum)

    if sumNum == int(N):  # 생성자이면 저장
        result = i
        break
    sumNum = 0

print(result)