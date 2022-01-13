########## 틀린 코드 ##########
'''
N = int(input())
body = []

for case in range(N):
    body.append(input().split()) # 몸무게, 키

for i in range(N): # 자신과 비교했을 때
    grade = 1
    for j in range(N):
        # 자신보다 키와 몸무게가 모두 큰 수가 몇인지만 구하면 됨
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            grade += 1
    print(grade, end=' ')
'''

########## 맞은 코드 ##########
N = int(input())
body = []

for case in range(N):
    body.append(input().split()) # 몸무게, 키

for i in range(N): # 자신과 비교했을 때
    grade = 1
    for j in range(N):
        # 자신보다 키와 몸무게가 모두 큰 수가 몇인지만 구하면 됨
        if int(body[i][0]) < int(body[j][0]) and int(body[i][1]) < int(body[j][1]):
            grade += 1
    print(grade, end=' ')

'''틀린 코드와 맞은 코드의 차이점... 그것은 문자열 비교 부분에 있었다!
body 리스트에 몸무게와 키를 문자열로 입력하게 되었고...
나는 숫자라 믿어 의심치 않았지만 문자열의 아스키 코드를 비교하고 있었던 것이다!
100 > 50 은 True지만 "100" > "50" 은 False이다. 타입에 대해 신경쓰도록 하자!'''