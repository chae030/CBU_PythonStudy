import math

s , n = input().split(' ')
total = 0
 
num = len(s)    #n진법 수 몇자리인지 

for i in range(num):
    # s[i]가 정수일 경우
    if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9') :    
        total += int(s[i]) * int(n) ** (num - i - 1)

    #s[i]가 A~Z 사이 문자일 경우 
    else:
        total += (ord(s[i]) - ord('A') + 10) * int(n) ** (num - 1 - i)
        
print(total)


