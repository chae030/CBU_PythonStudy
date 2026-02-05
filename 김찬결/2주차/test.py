import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
max_h = max(data)

for i in range(1, n - 1):
    height = min(data[i - 1], data[i + 1])
    result = data[i] + height

    max_h = max(max_h, result)

print(max_h)