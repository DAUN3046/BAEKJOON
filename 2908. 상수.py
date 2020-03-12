def reverseNumber(num):
    a1 = num//100 #백의 자리 숫자
    a2 = (num%100)//10 #십의 자리 숫자
    a3 = num%10 #일의 자리 숫자
    return a3*100+a2*10+a1

num1, num2 = map(int, input().split())
#print(num1, num2)
num1 = reverseNumber(num1)
num2 = reverseNumber(num2)
#print(num1, num2)

if num1 > num2:
    print(num1)
else:
    print(num2)