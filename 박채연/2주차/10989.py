# 계수정렬(Counting Sort)

import sys

readline = sys.stdin.readline

n = int(readline())
count = [0] * (10000+1)

for i in range(n) :
    x = int(readline())
    count[x] += 1

for i in range(1, len(count)) :
    count[i] += count[i-1]

result = [0] * n
c = count.index(max(count))

for i in range(c+1) :
    idx = count[i]
    result[idx-1] = i
    count[i] -= 1

print(result)
