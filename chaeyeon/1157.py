str = input()

str = str.upper()
result = {}

for s in str :
    if s not in result :
        result[s] = 1
    else :
        result[s] += 1

value = result.values()
m = max(value)
cnt = 0

for k, v in result.items() :
    if (v == m) :
        cnt += 1
        ans = k

if (cnt > 1) :
    print("?")
else :
    print(ans)