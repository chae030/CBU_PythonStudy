# 같은 눈 3개 : 10000 + 눈*1000
# 같은 눈 2개 : 1000 + 눈*100
# 모두 다른 눈 : 가장큰눈*100

num1, num2, num3 = map(int, input().split())

if ((num1 == num2) and (num2 == num3)) :
    print(10000 + num1*1000)
elif (num1 == num2) :
    print(1000+num1*100)
elif (num2 == num3) :
    print(1000+num2*100)
elif (num1 == num3) :
    print(1000+num3*100)
else :
    m = max(num1, num2, num3)
    print(m*100)
