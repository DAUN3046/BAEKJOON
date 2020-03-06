N = int(input())
add = 0
score = 0
line = []

for i in range(N):
    line = input()
    line_after = line.replace("O","1") #라인의 0를 1, X를 0로 라벨링
    line_after = line_after.replace("X","0")
    line_after = list(map(int, line_after))
    #print(line_after.count(1))
    for i in range(len(line_after)):
        if line_after[i] == 1:
            add += 1
            score += add
        else:
            add = 0
    print(score)
    score = 0
    add = 0