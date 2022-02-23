from collections import Counter
prize = [] # 상금 리스트

n = int(input())
for i in range(n):
    num_list = list(map(int, input().split()))
    num = Counter(num_list).most_common(1)[0][0] # 가장 많이 나온 수
    cnt = Counter(num_list).most_common(1)[0][1] # 가장 많이 나온 수의 빈도
    if cnt == 1: # 모두 다른 눈이 나온 경우
        prize.append(max(num_list)*100)
        # print("case1")
    elif cnt == 4: # 모두 같은 눈이 나온 경우
        prize.append(50000+num*5000)
        # print("case2")
    elif cnt == 3: # 같은 눈이 3개 나온 경우
        prize.append(10000+num*1000)
        # print("case3")
    elif Counter(num_list).most_common(2)[1][1] == 2: # 같은 눈이 2개인데 두 쌍씩 나온 경우
        prize.append(2000+num*500+Counter(num_list).most_common(2)[1][0]*500)
        # print("case4")
    elif cnt == 2: # 같은 눈이 2개만 나오는 경우
        prize.append(1000+num*100)
        # print("case5")
# print(prize)
print(max(prize))