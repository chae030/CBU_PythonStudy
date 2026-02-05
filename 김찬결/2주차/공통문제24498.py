# N개의 탑의 높이
# [1, 3, 2, 2]
# [1, 1, 4, 0]

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

max_h = max(A)

for i in range(1, N-1):
    add_h = min(A[i-1], A[i+1])
    result_h = A[i] + add_h

    max_h = max(result_h, max_h)

print(max_h)