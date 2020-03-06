# 한수의 예.123(등차가 1), 753(등차가 -2). 1~99는 모두 한수. 최대 3자리.

N = int(input())
numlist = []
cnt = 0

if N < 100:
    print(N)

else:

    for number in range(100, N + 1):
        number = str(number)

        for j in range(len(number)):  # numlist에 각 숫자 채우기
            numlist.append(int(number[j]))

        for i in range(1, 5):  # 증가되는 수열인 경우
            if (numlist[0] == numlist[1] + i) and (numlist[1] == numlist[2] + i):  # 각 자리수 비교하기
                cnt += 1

        for i in range(1, 5):  # 감소하는 수열의 경우
            if (numlist[0] + i == numlist[1]) and (numlist[1] + i == numlist[2]):
                cnt += 1

        if (numlist[0] == numlist[1]) and (numlist[1] == numlist[2]):
            cnt += 1

        # print(numlist, cnt)

        del numlist[:]  # 다음 숫자 들어와야 되니까 numlist 초기화

    print(99 + cnt)  # 결과값