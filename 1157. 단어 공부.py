word = input().rstrip()  # 문자 입력
word_list = list(word)  # 입력단어리스트화
result_list = []
cnt = 0

# 소문자일 경우 대문자로 변환
for i in range(len(word_list)):
    if word_list[i] in 'abcdefghijklmnopqrstuvwxyz':
        num = ord(word_list[i])
        word_list[i] = chr(num - 32)
# print("word_list:", word_list)

# 딕셔너리 생성
dic = {}
for word in word_list:
    dic[word] = 0
for count in word_list:
    dic[count] += 1

# print("dic:", dic)

result_list = list(dic.values()) # 빈도값들을 따로 리스트화
mode = max(result_list) # 최빈값 저장

for i in range(len(result_list)): # 최빈값이 몇 개인지 세는 변수 cnt 채우기
    if result_list[i] == mode:
        cnt += 1

# print("cnt:", cnt)

if cnt == 1: # 최빈값이 1개이면
    print(max(dic, key=dic.get)) #해당 값을 가져오기
else: # 2개 이상이면
    print("?") # 물음표 출력