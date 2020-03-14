X = int(input())
cnt = 0
num = 0
order = 0
while True:
    cnt += 1
    num += cnt # +1 +2 +3 +4 +5
    if X <= num:
        break
#print("cnt:", cnt, "num:", num)
order = num - X
if cnt % 2 == 1: #if count is odd number
    for i in range(cnt):
        if order == i:
            print(str(1 + i)+"/"+str(cnt - i))
else: #if count is even number, reverse this
    for i in range(cnt):
        if order == i:
            print(str(cnt - i)+"/"+str(1 + i))
