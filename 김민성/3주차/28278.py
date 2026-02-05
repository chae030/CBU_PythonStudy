# O(N)

import sys

s = []
for _ in range(int(input())):
    o, *x = map(int, sys.stdin.readline().rstrip().split())

    if o == 1:
        s.append(x[0])
    elif o == 2:
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif o == 3:
        print(len(s))
    elif o == 4:
        if len(s) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(s) == 0:
            print(-1)
        else:
            print(s[len(s)-1])
