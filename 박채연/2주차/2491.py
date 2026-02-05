n = int(input())
x = input()

arr = list(map(int, x.split()))
m = up = down = 1

for i in range(n-1) :
    if (arr[i] < arr[i+1]) : # 오름차순
        up += 1
        down = 1
    elif (arr[i] > arr[i+1]) : # 내림차순
        up = 1
        down += 1
    else : 
        up += 1
        down += 1
    m = max(m, up, down)
    
print(m)