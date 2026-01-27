import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int , input().split()))

increase = decrease = best = 1

for i in range(1, n):
    if arr[i-1] <= arr[i]:
        increase += 1
    else:
        increase = 1

    if arr[i-1] >= arr[i]:
        decrease += 1
    else:
        decrease = 1

    best = max(best , increase, decrease)

print(best)
