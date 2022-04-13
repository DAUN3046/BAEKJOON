def era(N): # 에라토스테네스의 체
    num, p = [False for _ in range(N+1)], [False for _ in range(N+1)]
    for i in range(2, N+1):
        if num[i] == True: continue
        p[i] = True
        for j in range(i*i, N+1, i):
            num[j] = True
    return p

T = int(input())
prime = era(10000)
diff = []

for _ in range(T):
    n = int(input())
    p_length = len(prime) # 1229
    for i in range(n // 2, 0, -1):
        j = n - i
        if prime[i] == True & prime[j] == True:
            print(i, j)
            break
'''
---------- 아래는 시행착오를 겪었던 시간 초과(9%) 코드 -----------
def era(N): # 에라토스테네스의 체
    num, prime = [False for _ in range(N+1)], []
    for i in range(2, N+1):
        if num[i] == True: continue
        prime.append(i)
        for j in range(i*i, N+1, i):
            num[j] = True
    return prime

T = int(input())
prime = era(10000)
for i in range(T):
    n = int(input())
    result = 0
    result_list = []
    for i in range(len(prime)):
        for j in range(i, len(prime)):
            if prime[i] + prime[j] == n:
                diff = abs(prime[i] - prime[j])
                result_list.append([i, j, diff])
    result_list.sort(key=lambda x: x[2])
    print(prime[result_list[0][0]], prime[result_list[0][1]])
'''