m, n = map(int, input().split())
tmt = []; t1 = []; t1w = []
maxc = 0;
for i in range(n):
    tmt.append(list(map(int, input().split())))
    for j in range(m):
        if tmt[i][j] != -1:
            maxc += 1
        if tmt[i][j] == 1:
            t1.append([i, j])
            t1w.append(0)

i = 0
while i < len(t1):
    x = t1[i][0]; y = t1[i][1]; w = t1w[i]
    if x > 0 and tmt[x-1][y] == 0:
            tmt[x-1][y] = 1
            t1.append([x-1, y])
            t1w.append(w+1)
    if x < len(tmt)-1 and tmt[x+1][y] == 0:
            tmt[x+1][y] = 1
            t1.append([x+1, y])
            t1w.append(w+1)
    if y > 0 and tmt[x][y-1] == 0:
            tmt[x][y-1] = 1
            t1.append([x, y-1])
            t1w.append(w+1)
    if y < len(tmt[x])-1 and tmt[x][y+1] == 0:
            tmt[x][y+1] = 1
            t1.append([x, y+1])
            t1w.append(w+1)
    i += 1

if len(t1) == maxc:
    print(t1w[len(t1)-1])
else:
    print(-1)