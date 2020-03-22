primeNumberList = [i for i in range(1, 1001)]
#print(primeNumberList)
primeNumberList[0] = 0
primeNumberList[3] = 0
for i in range(2, 1000):
    for j in range(1, 1000):
        if primeNumberList[j] != (i+1) and primeNumberList[j] % (i+1) == 0:
            primeNumberList[j] = 0

#print(primeNumberList)

count = 0
N = int(input())
numList = list(map(int, input().split()))
for i in range(len(numList)):
    if numList[i] in primeNumberList:
        count += 1
print(count)