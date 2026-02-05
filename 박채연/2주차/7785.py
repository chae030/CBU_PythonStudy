n = int(input())
dic = {}

for _ in range(n) :
    log = input()
    name, enter = log.split()
    if (enter == "enter") :
        dic[name] = 1
    elif (enter == "leave") :
        dic[name] = 0

name_list = []
for n,e in dic.items() :
    if (e) :
        name_list.append(n)
name_list.sort(reverse=True)
for l in name_list : 
    print(l)