n , b = map(int , input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = ""

while n > 0:
    n , r = divmod(n , b)   # n = 몫 , r = 나머지 
    ans = digits[r] + ans   # 앞에 붙이기 

print(ans)