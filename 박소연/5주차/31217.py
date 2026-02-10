import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u] += 1
    graph[v] += 1

y = 0
for i in range(1, n+1):
    if graph[i] >= 3:
        y += graph[i] * (graph[i]-1) * (graph[i]-2) // 6

print(y % (10**9 + 7))