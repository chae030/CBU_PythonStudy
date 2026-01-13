x = int(input())
n = int(input())
sum = 0

for _ in range(n) :
    i = input()
    a, b = map(int, i.split())
    sum += (a * b)
    
if (sum == x) :
    print("Yes")
else : 
    print("No")