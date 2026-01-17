n = int(input())
cnt = 0

for _ in range(n) :
    str = input()
    l = []
    for i in range(len(str)) :
        flag = 1
        if (str[i] in l) : # 이미 나온 적 있음
            if (str[i] == str[i-1]) : # 연속인 경우
                pass # OK
            else : # 연속이 아닌 경우
                flag = 0 # 안됑!
                break # 탈출
        else : # 나온 적 없음
            l.append(str[i]) # l에 추가, OK
    if (flag) :
        cnt += 1

print(cnt)