n, m = map(int, input().split())

n_list = [i for i in range(1, n+1)]
# print('초기 리스트:', n_list)
for _ in range(m):
  i, j = map(int, input().split())
  # print('바꿀 범위:', n_list[i-1:j])
  slice_list = n_list[i-1:j]
  reverse_list = slice_list[::-1]
  new_list = n_list[ : i-1] + reverse_list + n_list[j:]
  n_list = new_list
  # print(m,'번 째 변환 후 리스트:', n_list)
print(*n_list)
