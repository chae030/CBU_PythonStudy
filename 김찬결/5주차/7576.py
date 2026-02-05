import sys
from collections import deque
input = sys.stdin.readline

def solve():
    m, n = map(int, input().split()) # m(열 수):6, n(행 수):4
    tomato = [list(map(int, input().split())) for _ in range(n)]
    '''
    [
        [1 -1 7 8 5 4],
        [2 -1 6 7 4 3],
        [3 4 5 6 -1 2],
        [4 5 6 7 -1 1]
    ]
    '''
    queue = deque() # 큐를 이용
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1: # 익은 토마토가 있는 곳에 대해서
                queue.append((i, j)) # 그 위치를 큐에 추가

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue: # 큐에 뭔가가 있다면
        x, y = queue.popleft() # 하나씩 꺼냄
        for i in range(4): # 상,하,좌,우 방향으로 이동하여
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 범위 내 인지 확인하고
                if tomato[nx][ny] == 0: # 익지 않은 토마토가 있는 곳에 대해서
                    tomato[nx][ny] = tomato[x][y] + 1 # 이동하기 전의 값에 +1 증가
                    # 즉, 한번 이동하여 확인할 때마다 날짜가 하루씩 증가
                    queue.append((nx, ny)) # 그리고 이동 후의 위치를 다시 큐에 추가
    # 큐에 남아있는게 없을 때까지 반복한 결과 -> tomato리스트에 최소 날짜가 들어가 있음

    result = 0
    for line in tomato:
        for i in line:
            if i == 0: # 각 요소를 방문하면서 익지 않은 토마토가 있다면
                return -1
        result = max(result, max(line)) # tomato에서 가장 큰 값을 반환 = 최소 날짜
    return result - 1

if __name__ == "__main__":
    print(solve()) # 1 -> 4로 변경됐다면 3번 이동한 것이므로 -1 하여 날짜 출력