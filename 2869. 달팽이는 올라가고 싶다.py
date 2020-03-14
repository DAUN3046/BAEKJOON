count = 0
A, B, V = map(int, input().split())
n = (V - B) / (A - B) #(A-B)(n-1)>=V 식을 정리
#print(n)
if n == int(n):
    print(int(n))
else:
    print(int(n + 1))
