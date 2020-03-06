result_list = []  # 나머지 리스트
count_list = [0] * 42  # 카운트 리스트
# 각 리스트는 0으로 초기화

for i in range(0, 10):  # 입력과 나눗셈 연산
    x = int(input())
    result_list.append(x % 42)  # 나머지

for i in range(10):  # 존재하는 숫자 1로 라벨링
    for j in range(0, 42):  # 나머지 리스트 도는 루프
        if result_list[i] == j:  # 입력한 숫자의 나머지에 따라
            count_list[j] = 1  # 나머지 자리에 1 할당

# print(result_list)
# print(count_list)
print(count_list.count(1))  # 존재하는 숫자 라벨링한 값을 전부 합하면 서로 다른 숫자의 개수가 출력됨.