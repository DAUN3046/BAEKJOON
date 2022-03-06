def era(N): # 에라토스테네스의 체
    num, prime = [False for _ in range(N+1)], []
    for i in range(2, N+1):
        if num[i] == True: continue
        prime.append(i)
        for j in range(i*i, N+1, i):
            num[j] = True
    return prime

m = int(input())
n = int(input())

if n == 1:
    print(-1)
elif era(n) == era(m) and era(n)[-1] == n: # 소수가 하나일 땐 그대로 출력
    print(era(n)[-1])
    print(era(n)[-1])
else:
    result = [i for i in era(n) if i >= m]  # 범위 내의 소수 리스트
    # print("result list:", result)
    if result: # 소수가 존재하면
        print(sum(result))
        print(result[0])
    else: # 소수가 없으면
        print(-1)