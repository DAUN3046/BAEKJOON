M, N = map(int, input().split())

is_prime = [True] * (N + 1)
is_prime[0], is_prime[1] = False, False

for prime in range(N - M + 1):
    if is_prime[prime] == True:
        for not_prime in range(prime * 2, N + 1, prime):
            is_prime[not_prime] = False

for i in range(M, N + 1):
    if is_prime[i]:
        print(i)

# ------ 7%에서 시간초과 ------
# for num in range(M, N + 1):
#     divisor = 2
#     while divisor < num:
#         if num % divisor == 0:
#             break
#         if divisor > num ** 0.5:
#             print(num)
#             break
#         divisor += 1