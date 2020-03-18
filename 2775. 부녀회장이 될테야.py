T = int(input())
aptList = [[0 for _ in range(14)] for _ in range(14)] #14x14

for room in range(14):
    aptList[0][room] = room + 1 #0층 채우기

for floor in range(14): #1호는 무조건 1명
    aptList[floor][0] = 1
#print(aptList)

for floor in range(1, 14): #1층부터 14층까지
    for room in range(1, 14): #그외 호수들 채우기
        aptList[floor][room] += 1
        for i in range(1, room + 1):
            aptList[floor][room] += aptList[floor-1][i]
#print(aptList)

for test_case in range(T):
    k = int(input()) #층
    n = int(input()) #호
    n = n - 1
    print(aptList[k][n])
