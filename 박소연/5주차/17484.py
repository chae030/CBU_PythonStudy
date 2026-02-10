n, m = map(int, input().split())
score = [list(map(int, input().split())) for _ in range(n)]
dpl = [[0] * m for _ in range(n)]
dpc = [[0] * m for _ in range(n)]
dpr = [[0] * m for _ in range(n)]
for i in range(m):
    if i > 0:
        dpl[0][i] = score[0][i]
    if i < m-1:
        dpr[0][i] = score[0][i]
    dpc[0][i] = score[0][i]

for i in range(1, n):
    for j in range(m):
        if j > 0:
            dpl[i][j] = min(dpc[i-1][j], dpr[i-1][j-1]) + score[i][j]
        if j < m-1:
            dpr[i][j] = min(dpc[i-1][j], dpl[i-1][j+1]) + score[i][j]
        if j > 0 and j < m-1:
            dpc[i][j] = min(dpr[i-1][j-1], dpl[i-1][j+1]) + score[i][j]
        elif j > 0:
            dpc[i][j] = dpr[i-1][j-1] + score[i][j]
        elif j < m-1:
            dpc[i][j] = dpl[i-1][j+1] + score[i][j]
        
dpl[n-1][0] = dpl[n-1][1]
dpr[n-1][m-1] = dpl[n-1][m-2]
resl = min(dpl[n-1])
resr = min(dpr[n-1])
resc = min(dpc[n-1])
res = min(resl, resr, resc)

print(res)