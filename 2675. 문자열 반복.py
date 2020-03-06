T = int(input())

for i in range(T):

    R, S = input().split()
    R = int(R)
    # print(S)
    string_list = list(S)
    # print(string_list)

    for j in range(len(string_list)):
        print(string_list[j] * R, end='')
    print()