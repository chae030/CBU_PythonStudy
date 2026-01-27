# O(N^2 * M^2)

n, m = map(int, input().split())
f = [input() for _ in range(n)]
wf = list((f"{'WB' * 4}", f"{'BW' * 4}")*4)
bf = list((f"{'BW' * 4}", f"{'WB' * 4}")*4)
a = []
for i in range(8, n + 1):
    for j in range(8, m + 1):
        we = 0
        be = 0
        for k in range(i - 8, i):
            for l in range(j - 8, j):
                if f[k][l] != wf[k-i][l-j]:
                    we += 1
                if f[k][l] != bf[k-i][l-j]:
                    be += 1
        a.append(min(we, be))

print(min(a))
