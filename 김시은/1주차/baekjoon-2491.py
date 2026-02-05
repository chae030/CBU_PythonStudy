N = int(input())
numbers = list(map(int, input().split()))


if N == 1:
    print(1)
else:
    inc_len = 1
    dec_len = 1
    answer = 1

    for i in range(1, N):
        if numbers[i] >= numbers[i - 1]:
            inc_len += 1
        else:
            inc_len = 1

        if numbers[i] <= numbers[i - 1]:
            dec_len += 1
        else:
            dec_len = 1

        answer = max(answer, inc_len, dec_len)

    print(answer)
