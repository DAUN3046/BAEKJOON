'''
# 시간 초과
n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += len(str(i))
print(ans)
'''
#### 아래로 통과 코드 ####
# 로그 사용으로 연산 줄이기
n = int(input())
print(sum(map(lambda x: len(str(x)), range(1, n + 1))))
'''
# 직접 수로 계산
n = int(input())
l, ans = len(str(n)), 0
for i in range(1, l):
    ans += i * (10**i - 10**(i-1)) # 순서대로 1~9, 10~99 ... 자릿수 계산
    # print("ans1:", ans)
ans += l * (n-10**(l-1)+1)  # 제일 큰 자릿수의 나머지들을 계산

print(ans)'''