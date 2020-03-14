A, B, C = map(int, input().split())
if B != C:
    if A/(C-B) > 0:
        print(int(A/(C-B)) + 1)
    else:
        print(-1)
else:
    print(-1)