n = int(input())
group_cnt = n

for _ in range(n):
    word = input() # abccbc
    for i in range(len(word)-1):
        if word[i] != word[i+1] and word[i+1] in word[:i]:
            # 글자가 바뀌었고 그 바뀐 글자가 해당 단어에 이미 있던 경우
            group_cnt -= 1 # 그룹단어에서 제외시킴
            break # 그리고 for문 종료하여 다음 단어 입력받을 준비

print(group_cnt)