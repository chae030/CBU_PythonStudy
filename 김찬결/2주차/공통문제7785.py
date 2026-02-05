import sys
input = sys.stdin.readline

n = int(input())
data = set()

for i in range(n):
    name, log = input().split()
    if log == "enter": data.add(name)
    else: data.remove(name)

for name in sorted(data, reverse=True):
    print(name)