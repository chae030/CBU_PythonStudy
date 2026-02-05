import sys
input = sys.stdin.readline

# n: 행 수, m: 열 수
n, m = map(int, input().split())
chess = [[input().strip()] for _ in range(n)]

for i in range(n - 7): # n-7=3
    for j in range(8):
        for k in range(m - 7): # m-7=6
            for l in range(8):
                chess[j][l]
    
    chess[0:10], chess[1:11], chess[2:12]