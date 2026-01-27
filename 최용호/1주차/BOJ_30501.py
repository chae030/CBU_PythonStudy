x = int(input())
count = 0
answer = ""

for i in range(x):
    name = input()
    if 'S' in name : 
        count = count + 1
        answer = name

if(count == 1):
    print(answer)