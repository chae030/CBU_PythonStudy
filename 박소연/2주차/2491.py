n = int(input())
lst = list(map(int, input().split()))

maxl = 1
count = 1

for i in range(n-1):
    if lst[i] <= lst[i+1]:
        count += 1
        if count > maxl:
            maxl = count
    else:
        count = 1
        
count = 1

for i in range(n-1):
    if lst[i] >= lst[i+1]:
        count += 1
        if count > maxl:
            maxl = count
    else:
        count = 1
        
print(maxl)