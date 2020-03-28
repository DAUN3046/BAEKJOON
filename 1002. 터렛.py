from fractions import Fraction
from decimal import Decimal

T = int(input())

for test_case in range(T):
    x1, y1, r1, x2, y2, r2 = map(Decimal, input().split())
    r_before = ((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))**0.5
    # r = Fraction('r_before**0.5')
    print(r_before, r)
    #각 위치와 거리를 두 원의 꼭짓점과 반지름으로 생각
    if x1 == x2 and y1 == y2: #두 원이 같을 때
        if r1 == r2:  #거리가 같으면
            print(-1) #모든 지점에 위치 가능하다
        else: #거리가 다르면
            print(0) #존재 불가능하다
    else: #두 원의 꼭짓점이 다른 경우
        if r == r1 - r2 or r == r2 - r1: #한 원이 다른 원을 포함할 때
            print(0) #만나지 않는다

        elif r + r1 == r2 or r + r2 == r1: #두 원이 내접할 때
            print(1) #한 점에서 만난다

        elif r > r1 + r2: #각 꼭짓점의 거리가 두 원의 반지름의 합보다 클 때
            print(0) #만나지 않는다
        elif r == r1 + r2: #'' 같을 때
            print(1) #한 점에서 만난다
        else:
            print(2)