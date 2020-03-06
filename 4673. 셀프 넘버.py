n = 0
result = 0
alist = []


def d(n):  # 셀프넘버 계산
    result = 0
    n = str(n)
    for i in range(len(n)):
        result += int(n[i])
    n = int(n)
    result += n
    n = result
    return n


for i in range(1, 10001):  # 10000까지 숫자 있음
    alist.append(i)

for i in range(1, 10001):  # 생성자 있는 숫자 지우기
    if d(i) in alist:
        alist.remove(d(i))

for i in range(len(alist)):
    print(alist[i])