c = int(input())
caselist = []

for i in range(c) :
    a = list(map(int, input().split()))
    caselist.append(a)

result = []

for case in caselist :
    n = case[0]
    total = 0
    for i in range(1, len(case)) :
        total += case[i]
    avg = total / n
    cnt = 0
    for i in range(1, len(case)) :
        if (case[i] > avg) :
            cnt += 1
        else :
            continue
    percent = (cnt / n) * 100
    result.append(percent)

for r in result :
    print(f"{r:.3f}%")