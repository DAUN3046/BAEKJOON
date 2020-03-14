N = int(input())
num = 2
cnt = 0
if N == 1:
    print(1)
elif N >= 2 and N <= 7:
    print(2)
else:
    while True:
        cnt += 1
        num += 6*cnt
        if N <= num - 1:
            break
#    print("cnt:", cnt + 1, "num:", num)
    print(cnt + 1)