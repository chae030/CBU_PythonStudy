n, m = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())
    
result = [0] * 26
for i in range(n):
    for j in range(m):
        temp = 0
        temp += (i+1)*(j+1)*(2*n-i)*(2*m-j)
        temp += (n+i+1)*(j+1)*(n-i)*(2*m-j)
        temp += (i+1)*(m+j+1)*(2*n-i)*(m-j)
        temp += (n+i+1)*(m+j+1)*(n-i)*(m-j)
        
        result[ord(s[i][j]) - ord('A')] += temp
        
for i in range(26):
    print(result[i])