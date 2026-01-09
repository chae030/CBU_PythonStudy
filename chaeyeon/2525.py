t = input()
d = int(input())

h, m = map(int, t.split())

m += d
if (m >= 60) :
    h += (m // 60)
    m -= 60 * (m // 60)

if (h >= 24) :
    h -= 24

print(h, m)