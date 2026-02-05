import sys
input = sys.stdin.readline

n, m = map(int, input().split())
not_Heard = set([input().strip() for _ in range(n)])
not_Seen = set([input().strip() for _ in range(m)])

result = list(not_Heard & not_Seen)
result.sort()

print(len(result))
print(*result, sep='\n')