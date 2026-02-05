# 못풀었습니다 ㅠㅠ

b = [list(input()) for _ in range(5)]
stars = []
for i in range(5):
    for j in range(5):
        if b[i][j] == '*':
            stars.append([i, j])
k = len(stars)
count = 0

xs = sorted(stars[i][0] for i in range(k))
centerx = xs[k//2]
for i in range(k):
    if stars[i][0] < centerx:
        for j in range(centerx, stars[i][0], -1):
            if b[j][stars[i][1]] != '*':
                count += abs(j - stars[i][0])
                b[j][stars[i][1]] = '*'
                b[stars[i][0]][stars[i][1]] = '.'
                stars[i][0] = j
                break
    elif stars[i][0] > centerx:
        for j in range(centerx, stars[i][0]):
            if b[j][stars[i][1]] != '*':
                count += abs(j - stars[i][0])
                b[j][stars[i][1]] = '*'
                b[stars[i][0]][stars[i][1]] = '.'
                stars[i][0] = j
                break
            
ys = sorted(stars[i][1] for i in range(k))
centery = ys[k//2]
for i in range(k):
    if stars[i][1] < centery:
        for j in range(centery, stars[i][1], -1):
            if b[stars[i][0]][j] != '*':
                count += abs(j - stars[i][1])
                b[stars[i][0]][j] = '*'
                b[stars[i][0]][stars[i][1]] = '.'
                stars[i][1] = j
                break
    elif stars[i][1] > centery:
        for j in range(centery, stars[i][1]):
            if b[stars[i][0]][j] != '*':
                count += abs(j - stars[i][1])
                b[stars[i][0]][j] = '*'
                b[stars[i][0]][stars[i][1]] = '.'
                stars[i][1] = j
                break

print(count)