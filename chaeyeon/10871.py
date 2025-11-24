n, x = map(int, input().split())
a = list(map(int, input().split()))
list = []

for r in a :
    if (r < x) :
        list.append(r)

for l in list :
    print(l, end=" ")