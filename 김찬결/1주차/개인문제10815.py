import sys
input = sys.stdin.readline

N = int(input()) # 숫자카드 개수 (최대50만개)
have_card = set(map(int, input().split())) # set은 순서가 없음

M = int(input()) # 숫자카드 개수 (최대50만개)
compare_card = list(map(int, input().split())) # set은 순서가 없음

for card in compare_card:
    print(1 if card in have_card else 0, end=' ')