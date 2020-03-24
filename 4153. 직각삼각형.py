while True:
    numList = list(map(int, input().split()))
    O = max(numList)
    numList.remove(O)
    M = numList[0]
    N = numList[1]
    if M==0 and N==0 and O==0:
        break
    if M*M + N*N == O*O:
        print("right")
    else:
        print("wrong")