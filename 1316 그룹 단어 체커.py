# 런타임 에러나는 코드

words = []

N = int(input()) # 단어의 개수
cnt = N # 그룹 단어가 아닌 것을 제하는 방식
for i in range(N):
    words.append(input()) # 각 단어 입력
for word in words: # 알고리즘
    length = len(word)
    for idx in range(length):
        if length == 1 or word[idx] not in ckList: # 처음 등장한 글자 넣음
            ckList.append(word[idx])
#             print("ckList:", ckList)
        else: # 이미 있는 글자일 때 이전 글자와 다르다면 그룹 단어가 아님
            if word[idx - 1] != word[idx]: 
                cnt -= 1
#                 print(word[idx-1], word[idx], "cnt:", cnt)
                break
    ckList = []

print(cnt)
