def era(N): # 에라토스테네스의 체
    num, prime = [False for _ in range(N+1)], []
    for i in range(2, N+1):
        if num[i] == True: continue
        prime.append(i)
        for j in range(i*i, N+1, i):
            num[j] = True
    return prime

def num_prime(n): # 소수의 개수 반환
    result = 0  # 개수
    # print(prime[:10])
    for i in prime:
        if (i >= n + 1) & (i <= 2*n):
            result += 1
        if (i > 2*n + 1):
            break
    return result

prime = era(123456*2 + 1)

while True:
    N = int(input())
    if N == 0: break
    print(num_prime(N))