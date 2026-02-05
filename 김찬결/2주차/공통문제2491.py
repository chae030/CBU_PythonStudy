import sys
input = sys.stdin.readline

n = int(input())
acs_cnt = 1
dec_cnt = 1
max_len = 1

data = list(input().split()) # 4, 1, 3, 3, 2, 2, 9, 2, 3
for i in range(1, n):
    if data[i-1] >= data[i]:
        dec_cnt += 1
    else: dec_cnt = 1

    if data[i-1] <= data[i]:
        acs_cnt += 1
    else: acs_cnt = 1

    max_len = max(max_len, dec_cnt, acs_cnt)
print(max_len)