a , b = map(int , input().split())

reversed_a = (a // 100) + (a % 100) // 10 * 10 +  a % 10 * 100 

reversed_b = (b // 100) + (b % 100) // 10 * 10 +  b % 10 * 100 

print( reversed_a if reversed_a > reversed_b else reversed_b)