########## 런타임 에러나는 코드 ##########

words = []

N = int(input()) # 단어의 개수
cnt = N # 그룹 단어가 아닌 것을 제하는 방식
for i in range(N):
    words.append(input()) # 각 단어 입력
for word in words:
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


########## 해결방법 ##########
# 1. 리스트 삭제. 굳이 필요가 없었다.

N = int(input()) # 단어의 개수
cnt = N # 그룹 단어가 아닌 것을 제하는 방식
for i in range(N):
    word = input() # 각 단어 입력
    length = len(word)
    for idx in range(length - 1): # N이 자연수여서 범위 가능
        if word[idx] == word[idx + 1]:
            pass
        elif word[idx] in word[idx+1:]: # 다른 글자가 나온 뒤 이전의 글자가 또 나오면 그룹 단어가 아님
            cnt -= 1
            break
    ckList = []

print(cnt)

# 여기서 range(0) 은 empty list를 반환하기에 결과적으로 길이가 1인 단어가 입력될 경우 그룹 단어로 상정된다.


# + 리스트 컴프리헨션을 이해하기 좋은것 같아 해당 번호 숏코딩 링크를 추가함. https://www.acmicpc.net/board/view/80793
