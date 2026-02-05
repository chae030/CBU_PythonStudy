# 시간복잡도: O(n)인 줄 알았으나,,
# 전체반복문이 종료되는 시점은 break를 만나는 순간임. 즉, 그 과정을 따라가보면
# spare % 3 == 0가 아니면 spare에 +5씩해서 다음 반복실행. 즉, spare % 3의 값이 (1 or 2)
# 하지만 spare % 3 == 0가 맞으면 0 임. 즉, ..->0->1->2->0->.. 의 반복이 일어남.
# 정리하자면 최대 3번안에는 나머지가 0임이 걸리게 되어있음.
# 따라서 "시간복잡도는 O(1)"

import sys
input = sys.stdin.readline

n = int(input())
five_cnt = n // 5  # 3

while five_cnt >= 0:
    spare = n - (5 * five_cnt)

    if spare % 3 == 0:
        three_cnt = spare // 3
        print(five_cnt + three_cnt)
        break
    else:
        five_cnt -= 1
else:
    print(-1)

# 12 -> 5 x 0 , 3 x 4 : 4