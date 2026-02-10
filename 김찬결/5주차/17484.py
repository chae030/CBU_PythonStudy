import sys
input = sys.stdin.readline

# DP(다이나믹 프로그래밍)
# 1. 큰 문제를 작은 문제로 나눌 수 있으며, 작은 문제의 답을 모아 큰 문제를 해결할 수 있음
# 2. 동일한 작은 문제를 반복적으로 해결해야 함

n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]

INF = float('inf')
dp = [[[INF] * 3 for _ in range(m)] for _ in range(n)]
# 왼쪽 위에서 이동: 0, 바로 위에서 이동: 1, 오른쪽 위에서 이동: 2
# ex) dp[0][0][1]: 현재 (0,0)좌표이고 바로 위에서 이동했다는 의미
# -> 즉, 현재의 상황을 통해 위의 상황을 판단가능(이동방향이 겹치면 안되기 때문)

for j in range(m):
    for i in range(3):
        dp[0][j][i] = space[0][j]
# 첫번째 행에서 출발이므로 첫 행 초기화

for i in range(1, n):
    for j in range(m):
    # dp 1행 1열부터 돌면서 달까지의 최소 연료 값을 계산
    # (i, j)는 이동한 후의 좌표로 취급
    
        if j > 0:
        # 1. 왼쪽 위에서 이동한 경우, 이동 전의 열이 0보다 커야함
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + space[i][j]
        
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][1]) + space[i][j]
        # 2. 바로 위에서 이동한 경우, 전체 열에서 가능

        if j < m - 1:
        # 3. 오른쪽 위에서 이동한 경우, 이동 전의 열이 m-1 보다 작아야 함
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + space[i][j]
'''한 행씩 넘어갈 때마다
[5,5,5]	  [8,8,8]	 [5,5,5]   [1,1,1]
[11,8,13] [10,13,10] [13,10,6] [9,6,INF]
[...]	  [17,19,19] [...]	   [...]
꼴로 저장됨'''
# dp 맨 마지막 행에 총 연료값들이 계산되어있음

for j in range(m):
    result = min(result, min(dp[n-1][j]))
    # 각 열의 최소값들끼리 비교하여 가장 작은 연료 값 출력
print(result)