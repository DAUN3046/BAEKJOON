N = int(input())  # 과목갯수 N개 입력
num = list(map(int, input().split()))  # 점수들 입력
M = max(num)

for i in range(N):  # 점수 조작 연산
    num[i] = num[i] / M * 100

print(sum(num) / N)  # 새로운 평균 연산