n = int(input())

for i in range(n):
    acc = 0
    count = 0
    l = str(input())
    
    for j in range(len(l)):
        if l[j] == 'O':
            acc += 1
            count += acc
        else:
            acc = 0
            
    print(count)