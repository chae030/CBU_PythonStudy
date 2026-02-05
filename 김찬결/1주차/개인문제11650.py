import sys
input = sys.stdin.readline

results = []

cnt = int(input())
for i in range(cnt):
    x,y = map(int, input().split())
    results.append((x ,y))

results.sort()

for i in range(cnt):
    print(results[i][0], results[i][1])