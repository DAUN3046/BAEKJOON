# 한 숫자씩 더한다.

N = int(input())
numbers = input()
result = 0

for i in range(N):
    result += int(numbers[i])

print(result)