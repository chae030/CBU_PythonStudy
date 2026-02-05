# 시간복잡도: O(mn) (8x8=64같은 상수의 경우에는 무시함)

import sys
input = sys.stdin.readline

m, n = map(int, input().split()) # 10, 13
chess = [list(input().strip()) for _ in range(m)]
result = [] # 다시 칠해야 하는 정사각형 개수 담는 공간

for i in range(m - 7): # 0, 1, 2
    for j in range(n - 7): # 0, 1, 2, 3, 4, 5, 6
        b_cnt = 0 # B시작 체스판일때의 색깔이 다를 때 추가하는 벌점
        w_cnt = 0 # W시작 체스판일때의 색깔이 다를 때 추가하는 벌점
        for a in range(i, i + 8):     # 8줄
            for b in range(j, j + 8): # 8줄
                if (a + b) % 2 == 0: # 짝수번째 or 대각선번째
                    if chess[a][b] != 'B': # B시작으로 가정했을 때, B가 아니면
                        b_cnt += 1 # B로 칠해야 하는 개수 +1 씩 증가
                    if chess[a][b] != 'W': # W시작으로 가정했을 때, W가 아니면
                        w_cnt += 1
                if (a + b) % 2 != 0: # 홀수번째
                    if chess[a][b] != 'W': # B시작으로 가정했을 때,
                        b_cnt += 1
                    if chess[a][b] != 'B': # W시작으로 가정했을 때,
                        w_cnt += 1
        result.append(min(b_cnt, w_cnt))
print(min(result))