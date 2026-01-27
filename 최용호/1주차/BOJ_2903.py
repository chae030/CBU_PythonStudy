import math

n = int(input())
ary = {}
ary[0] = 4

for i in range(1 , 16 , 1) :
    ary[i] = (math.sqrt(ary[i-1]) * 2 - 1) ** 2

print(f"{ int (ary[n]) }")