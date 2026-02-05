# O(nlogn + m)

n, m = map(int, input().split())
h = 24*n
mins = list(map(int, input().split()))
k = list(map(int, input().split()))
d = [0] * 101
res = sum(mins)

ls = sorted(zip(k, mins))
ls.reverse()

for i in range(m):
    b = ls[i][0]
    a = ls[i][1]
    
    d[b] += (100-a)//b
    d[(100-a)%b] += 1
    
for i in range(100, 0, -1):
    if h <= 0:
        break
    if d[i] < h:
        res += i*d[i]
        h -= d[i]
    else:
        res += i*h
        h = 0
        
print(res)