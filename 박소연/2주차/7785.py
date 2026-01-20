import sys
input = sys.stdin.readline

n = int(input())
pl = set()

for _ in range(n):
    name, ch = input().split()
    if ch == "enter":
        pl.add(name)
    else:
        pl.remove(name)
        
for name in sorted(pl, reverse=True):
    print(name)