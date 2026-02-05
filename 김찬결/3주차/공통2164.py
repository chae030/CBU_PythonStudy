# 각 함수들은 O(1)이지만, while문을 돌면서 n번정도 실행되기 때문에
# 시간 복잡도: O(n) (50만 번 정도 수행하면 0.1~0.2초 내에 끝남)

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
card = deque(range(1, n + 1))

while len(card) > 1: # 덱의 요소가 수천만개이상이어도 O(1)
        card.popleft() # 첫번째 값을 제거
        card.append(card.popleft())

print(card[0])


"""
계속 시간초과 발생.. 뭐가 문제일까?
pop(0) 또는 insert(0, x)는 성능적으로 매우 불리한 연산
why? 삭제 혹은 추가 시 모든 데이터를 당기거나 밀어줘야 함
=> 시간복잡도: O(n)

따라서 양방향에서 추가하고 제거할 수 있는 자료구조 deque(덱)를 사용
" from collections import deque "
deque는 appendleft(x)를 제공 -> x를 첫번째 데이터로 삽입 가능
deque는 popleft()를 제공 -> 첫번째 데이터 제거 가능
오른쪽 기준 시 append(x), pop(x) 사용
=> 시간복잡도: O(1)
"""

"""
NameError발생.. 뭐가 문제일까?
기존코드에서 n == 1 일때 popleft()를 두번 연속으로 함 -> 뺄게 없으니 인덱스오류가 발생하는 것
따라서, 이 부분을 해결해주는 while (조건문)을 사용 -> 카드의 개수가 2개 이상일때만 반복
"""