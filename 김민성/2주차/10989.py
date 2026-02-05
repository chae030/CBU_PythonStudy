import sys

c = [0 for _ in range(10000)]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    c[n - 1] += 1

i = 0
while i < len(c):
    if c[i] == 0:
        i += 1
        continue
    sys.stdout.write(f"{i + 1}" + "\n")
    c[i] -= 1
