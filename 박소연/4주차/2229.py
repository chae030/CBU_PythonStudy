# O(n^2)

n = int(input())
score = list(map(int, input().split()))
dp = [0] * n

for i in range(0, n):
    maxs = score[i]
    mins = score[i]
    for j in range(i+1, n):
        maxs = max(maxs, score[j])
        mins = min(mins, score[j])
        if i != 0:
            dp[j] = max(dp[j], (dp[i-1]+(maxs-mins)))
        else:
            dp[j] = max(dp[j], (maxs-mins))
            
print(dp[n-1])