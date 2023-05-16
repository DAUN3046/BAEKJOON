n, m = map(int, input().split())
num_list = [num for num in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    num_list[i - 1], num_list[j - 1] = num_list[j - 1], num_list[i - 1]

print(*num_list)
