import sys
input = sys.stdin.readline

N = int(input()) # 10

# dp[i] : i를 1로 만드는 최소 연산 횟수를 저장할 리스트
dp = [0] * (N+1)

for i in range(2, N+1):
    # 1을 빼는 경우를 기본값으로 저장 (비교할 때 기준이 되는 것)
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0: dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0: dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])