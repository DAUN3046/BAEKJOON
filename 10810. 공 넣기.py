n, m = map(int, input().split())
ball_list = [0 for i in range(n)]

for i in range(m):
  i, j, k = map(int, input().split())
  for _ in range(n):
    for val in range(i-1, j):
      ball_list[val] = k

print(*ball_list)
