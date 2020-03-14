def groupWord(word):
   wordList = list(word)
   print(wordList)


N = int(input())
count = 0
for test_case in range(N):
    word = input()
    if groupWord(word) == True:
        count += 1
        print("result count:", count)
#print(count)