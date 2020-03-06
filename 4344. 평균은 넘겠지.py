C = int(input())
sum_score = 0
rate = 0
count = 0

for i in range(C):
    score = list(map(int, input().split()))
    # score[0]는 과목의 수이고 score[1]~ 과목의 점수들

    for i in range(1, score[0] + 1):  # 평균 계산
        sum_score += score[i]
        # print(sum_score)
    avg = sum_score / score[0]
    # print(avg)
    for i in range(1, score[0] + 1):  # 비율 계산 후 출력
        if score[i] > avg:
            count += 1
    rate = round((count / score[0]) * 100, 3)
    print("%.3f" % (rate) + "%")
    sum_score = 0
    rate = 0
    count = 0