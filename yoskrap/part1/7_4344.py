c = int(input())

for i in range(c):
    l = list(map(int, input().split()))
    lsum = 0
    ssum = 0
    
    for j in range(l[0]):
        lsum += l[j+1]
        
    for j in range(l[0]):
        if (lsum/l[0]) < l[j+1]:
            ssum += 1
            
    print(str(round((ssum/l[0])*100, 3))+"%")