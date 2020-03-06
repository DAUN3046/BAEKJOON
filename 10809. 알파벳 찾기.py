S = input()
small_letter = 'abcdefghijklmnopqrstuvwxyz'
result = [-1]*len(small_letter) #abcdefghijklmnopqrstuvwxyz 각 자리에 몇개있냐
# result[2] = 3 #리스트 원소 변경법

for i in range(len(S)): #baekjoon
    for j in range(len(small_letter)): #abcd~
        if S[i] == small_letter[j]:
            if result[j] == -1:
                result[j] = i

for i in range(len(result)-1):
    print(result[i], end=' ')
print(result[-1])