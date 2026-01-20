n = int(input())
lst = list(map(int, input().split()))

maxn = max(lst[0], lst[n-1])

for i in range(1, n - 1):
    temp = min(lst[i - 1], lst[i + 1])
    maxn = max(maxn, temp + lst[i])

print(maxn)