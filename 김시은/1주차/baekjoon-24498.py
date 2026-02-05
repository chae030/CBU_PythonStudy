N = int(input())
A = list(map(int, input().split()))

answer = max(A)

for i in range(1, N - 1):

    left_sum = 0
    for l in range(i - 1, -1, -1):
        left_sum += A[l]
        if left_sum < i - l:
            break
    left_possible = left_sum

    right_sum = 0
    for r in range(i + 1, N):
        right_sum += A[r]
        if right_sum < r - i:
            break
    right_possible = right_sum

    moves = min(left_possible, right_possible)
    answer = max(answer, A[i] + moves)

print(answer)
