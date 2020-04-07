# brute force algorithm

N, M = map(int, input().split())
numList = list(map(int, input().split()))
hap = 0
hap1 = 0
hap2 = 0
numList_copy = []
numList123 = []
for i in range(N):
    hap = 0
    numList_copy = numList.copy()
    hap += numList_copy[i]
    # print("hap:", hap)
    numList_copy[i] = 0
    for j in range(N):
        if numList_copy[j] != 0:
            hap1 = hap + numList_copy[j]
            # print("hap1:", hap1)
            numList_copy[j] = 0
            for k in range(N):
                if numList_copy[k] != 0:
                    hap2 = hap1 + numList_copy[k]
                    # print("hap2:", hap2)
                    if hap2 <= M:
                        numList123.append(hap2)
                        # print("i, j, k, hap2:", i, j, k, hap2)

# print(numList123)
print(max(numList123))
