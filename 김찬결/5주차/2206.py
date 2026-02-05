import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
'''
[
    [0,1,0,0],
    [1,1,1,0],
    [1,0,0,0],
    [0,0,0,0],
    [0,1,1,1],
    [0,0,0,0]
]
'''
count = 0
queue = deque()

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
        if 0 <= nx < m and 0 <= ny < n:
            if matrix[nx][ny] == 1:
                while True:
                    
                matrix[nx][ny] = 0
for i in range(0, m):
    for j in range(0, n):
        if matrix[i][j] == 0:
            dfs(i, j)
            count += 1