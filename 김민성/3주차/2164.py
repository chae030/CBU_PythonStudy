# O(N)

import collections

n = int(input())

card = collections.deque([i for i in range(1, n+1)])

while len(card) > 1:
    card.popleft()
    move = card.popleft()
    card.insert(len(card), move)

print(card[0])
