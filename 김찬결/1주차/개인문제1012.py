import sys
input = sys.stdin.readline

T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = [(x, y)]
    graph[x][y] = 0 # 방문 표시 (0으로 변경)
    
    while queue:
        ex, ey = queue.pop(0)
        for i in range(4):
            nx = ex + dx[i]
            ny = ey + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0 
                    queue.append((nx, ny))

results = []
for _ in range(T): # 테스트 케이스만큼 반복
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                cnt += 1
                bfs(i, j)
    results.append(cnt)

print(*results, sep='\n')