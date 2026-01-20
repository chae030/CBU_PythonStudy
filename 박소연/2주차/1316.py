n = int(input())
count = 0

for _ in range(n):
    word = input()
    alp = [0] * 26
    check = 1
    l = len(word)
    
    for i in range(l-1):
        index = ord(word[i+1]) - ord('a')
        if alp[index] == 1:
            if word[i] != word[i+1]:
                check = 0
                break
        alp[ord(word[i]) - ord('a')] = 1
        alp[index] = 1
        
    if check == 1:
        count += 1
        
print(count)