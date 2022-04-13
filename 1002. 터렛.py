T = int(input())

for test_case in range(T):
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    distance = float((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))**0.5
    #각 위치와 거리를 두 원의 꼭짓점과 반지름으로 생각
    if distance > r1 + r2: # 두 원이 만나지 않음
        print(0)
    elif distance == r1 + r2: # 두 원이 겹치지 않게 한 점에서 만남
        print(1)
    elif distance < r1 + r2: # 두 원이 교차하거나 포함됨
        if (x1 == x2) & (y1 == y2):
            if r1 == r2: # 두 원이 같음
                print(-1)
            else: # 포함관계로 만나지 않음
                print(0)
        elif distance == abs(r1 - r2): # 내접
            print(1)
        elif distance < abs(r1 - r2): # 포함되어서 만나지 않음
            print(0)
        else: # 두 원이 두 교점을 가짐
            print(2)