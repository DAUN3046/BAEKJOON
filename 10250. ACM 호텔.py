T = int(input())
roomFloor = 0
roomNum = 0
for i in range(T):
    H, W, N = map(int, input().split()) #층, 호수, 순서
    roomNum = N // H + 1
    roomFloor = N % H
    if roomFloor == 0:
        roomFloor = H
        roomNum -= 1 # 1번째부터 세기 때문에 존재하던 0번째를 제거하여 한 칸씩 뺀다.
    print(roomFloor*100 + roomNum)