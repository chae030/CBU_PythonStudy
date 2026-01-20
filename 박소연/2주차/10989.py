import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10000

for _ in range(n):
    count[int(input()) - 1] += 1

for i in range(10000):
    for _ in range(count[i]):
        print(i + 1)