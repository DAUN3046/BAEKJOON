idx = 0  # 인덱스 변수
count_list = []  # 문자개수리스트

word = input().rstrip()  # 문자 입력
word_list = list(word)  # 입력단어리스트화

for i in range(len(word_list)):
    if word_list[i] in 'abcdefghijklmnopqrstuvwxyz':  # 소문자일 경우 대문자로 변환
        num = ord(word_list[i])
        word_list[i] = chr(num - 32)
# print(word_list)

#=======================================================================================================================

for i in range(len(word_list)):  # 문자열의 길이만큼
    # count_list.append(word_list.count(word_list[i]))  # 문자의 개수를 리스트에 넣는다.
    for j in range(len(word_list)):
        count_list[j] += 1

print("count_list:", count_list)  # 확인. 후에 지우기.
many_word = max(count_list)

print("many_word:", many_word)  # 확인. 후에 지우기.
print(many_word)  # 확인. 후에 지우기.
idx = count_list.index(many_word)
int(idx)

keynum_count = count_list.count(many_word)  # 리스트 내 최빈값
print("keynum_count:", keynum_count)  # 확인. 후에 지우기.
print("========")  # 확인. 후에 지우기

# a의 아스키 코드는 97, A의 아스키 코드는 65이다.
if many_word != keynum_count:
    print("?")
else:
    print(word_list[idx])  # 아니면 그대로 출력