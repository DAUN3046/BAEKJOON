N = int(input())
num5 = N//5
num3 = N//3
numList = []
for i in range(0, num5 + 1):
    for j in range(0, num3 + 1):
        calculate = 5*i + 3*j
        #print("i=", i, "j=", j, "calculate:", calculate)
        if calculate == N:
            numList.append(i+j)
            break
        else:
            pass
if len(numList) >= 1:
    print(min(numList))
else:
    print(-1)
