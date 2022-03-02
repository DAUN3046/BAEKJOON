a, b = map(int, input().split()) # 시작 시간
c = int(input()) # 소요시간

b += c
while b >= 60:
    a += 1
    b -= 60
    if a == 24: a = 0
print(a, b)