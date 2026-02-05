"""
1. 아이디어
- 2중 for문 -> 값 1, 방문X -> BFS 이용

2. 시간 복잡도
- BFS : O(V+E) | V : m*n = 500*500 | E : 4*m*n = 4*500*500
- V+E : 5*250000 = 약 125만, 125만 << 1억 => 연산 가능

3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
chk = [[False] * M for _ in range(N)]

cnt = 0
maxSize = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 시작 좌표에서 상하좌우로 연결된 모든 칸을 찾아 방문 처리를 하고, 그 그림의 넓이를 계산해 반환하는 함수
def bfs(y, x):
    
    res = 1
    q = [(y,x)]
    while q:
        ey, ex = q.pop(0)
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<N and 0<=nx<M:
                if grid[ny][nx] == 1 and chk[ny][nx] == False:
                    res += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))
    return res

for j in range(N):
    for i in range(M):
        if grid[j][i] == 1 and chk[j][i] == False:
            # 방문흔적 남김
            chk[j][i] = True
            # 전체 그림 갯수를 +1
            cnt += 1
            # BFS => 그림 크기를 구해주고 최대값 갱신
            maxSize = max(maxSize, bfs(j,i))

print(cnt)
print(maxSize)