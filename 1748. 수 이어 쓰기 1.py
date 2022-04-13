# 직접 수로 계산
n = int(input())
length, ans = len(str(n)), 0
for i in range(1, length):
    ans += i * (10**i - 10**(i - 1))
    # 1 ~ 9, 11 ~ 99, ... 계산식 i * (10 ** i - 1 - 10 ** (i - 1) + 1)
# 제일 큰 자릿수 남은 숫자들 계산
ans += length * (n - 10**(length-1) + 1)
print(ans)

'''
# 시간 초과
n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += len(str(i))
print(ans)
'''
''' 로그 사용
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum = sum + int(math.log10(i)) + 1
print(sum)
'''