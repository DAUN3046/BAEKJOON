x, y, w, h = map(int, input().split())
if w - x > h - y:
    result = h - y
else:
    result = w - x
if x > y:
    result1 = y
else:
    result1 = x
if result > result1:
    print(result1)
else:
    print(result)