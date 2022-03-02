def result(nun):
    sorted(nun)
    if len(set(nun)) == 1: # 셋 다 같은 눈
        return 10000 + nun[0] * 1000
    elif len(set(nun)) == 3: # 셋 다 다른 눈
        return max(nun) * 100
    else: # 두 개만 같은 눈
        if nun[0] == nun[1]:
            return 1000 + nun[0] * 100
            # 1 1 2, 1 2 1, 2 1 1
        return 1000 + nun[2] * 100

nun = list(map(int, input().split()))
print(result(nun))