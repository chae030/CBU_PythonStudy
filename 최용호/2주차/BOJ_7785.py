import sys
input = sys.stdin.readline

n = int(input())
enter_set = set()

for i in range(n):
    name , log = input().split()
    if log == "enter" : 
        enter_set.add(name)
    else :
        enter_set.discard(name)

out = sorted(enter_set, reverse = True)

for i in out : 
    print(i)

