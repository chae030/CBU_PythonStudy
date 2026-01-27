import sys
input = sys.stdin.readline

n = int(input())
ans = 0

for i in range(n) :
    word = input()
    seen = set()
    prev = ' '

    ok = True

    for j in word : 
        if j != prev:       # 새 문자가 되는 순간 
            if j in seen :      # 예전에 썻던 놈이면 false
                ok = False
                break
            else :
                seen.add(j)         #처음보는 문자로 기록
                prev = j        #이전 단어 갱신 

    if ok :
        ans += 1

print(ans)