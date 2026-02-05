'''# 나의 코드
import sys
input = sys.stdin.readline

N = int(input())
word_list = []

for i in range(N): # max 20000번
    word = input().strip()
    if word not in word_list: # max 20000번 => 전체 복잡도가 O(N^2)
        word_list.append(word.lower())

word_list.sort(key= lambda x : (len(x), x))
print(*word_list, sep='\n')
'''

# 추천 코드
import sys
input = sys.stdin.readline

N = int(input())
word_list = list(set(input().strip() for _ in range(N)))
word_list.sort(key= lambda x: (len(x), x))

print(*word_list, sep='\n')