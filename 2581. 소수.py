cnt = 0
hapList = []
hap = 0

M = int(input())  # M <=
N = int(input())  # <= N

primeNumberList = [i for i in range(1, 10001)]
#print(primeNumberList)
primeNumberList[0] = 0
primeNumberList[3] = 0
for i in range(2, 10000):
    for j in range(1, 10000):
        if primeNumberList[j] != (i+1) and primeNumberList[j] % (i+1) == 0:
            primeNumberList[j] = 0
#print(primeNumberList)

primeNumberList2 = primeNumberList[M-1:N-1]
print("primeNumberList2:", primeNumberList2)

for i in range(len(primeNumberList2)):
    if primeNumberList2[i] != 0:
        hapList.append(primeNumberList2[i])

print("hapList:", hapList)

for i in range(len(hapList)):
    hap += hapList[i]

if len(hapList) == 0:
    print(-1) #소수가 없는 경우
else:
    print(hap) #전체 합
    print(hapList[0]) #최솟값