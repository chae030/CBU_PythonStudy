import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

count = 0
for i in range(n - 1, -1, -1):
    if k >= coins[i]:
        quo = k // coins[i]
        count += quo
        k = k % coins[i]

    if k == 0:
        break

print(count)