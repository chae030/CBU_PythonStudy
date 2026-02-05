# 시간복잡도: O(1)

import sys
input = sys.stdin.readline

n = int(input()) # 9
chair = input().strip().replace('LL', 'M')

holder_cnt = len(chair) + 1 # 컵홀더 개수: 7

# 컵홀더의 개수가 인원수보다 많은 경우 인원수대로 ㄱ
# 인원수가 컵홀더의 개수보다 많은 경우 컵홀더개수 ㄱ

print(min(holder_cnt, n))