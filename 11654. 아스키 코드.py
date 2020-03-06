s = input()
big_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_letter = 'abcdefghijklmnopqrstuvwxyz'
number = '0123456789'

if s in big_letter:  # 대문자인 경우
    print(65 + big_letter.index(s))

if s in small_letter:  # 소문자인 경우
    print(97 + small_letter.index(s))

if s in number:  # 숫자인 경우
    print(48 + number.index(s))