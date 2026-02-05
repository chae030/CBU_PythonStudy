T = int(input())

for i in range(T):
    cnt = 0
    vps = input().strip()

    for char in vps:
        if char == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt == -1:
                break
    print("YES" if cnt == 0 else "NO")