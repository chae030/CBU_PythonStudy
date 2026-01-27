s = input().strip()

ary = ['ABC' , 'DEF' , 'GHI' , 'JKL' , 'MNO' , 'PQRS' , 'TUV' , 'WXYZ']
result = 0

for i in range(len(s)):
    for j in range(8):
        if s[i] in ary[j]:
            result += j + 3

    
print(result)