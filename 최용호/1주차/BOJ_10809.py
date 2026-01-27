s = input()     #단어 입력받기 
ary = [-1] * 26       # 알파벳 리스트

for i in range(len(s)) :
    if ary[ord(s[i]) - ord('a')] != -1:     #ord 함수로 문자를 정수로 변환 
        continue
    else : 
        ary[ord(s[i]) - ord('a')] = i

for i in range(26) :
    print(ary[i], end = ' ')
