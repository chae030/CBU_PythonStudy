#ary에 피보나치 함수 값 저장 
ary = [-1] * 41

ary[0] = 0
ary[1] = 1

def fibo(n):
    if ary[n] != -1:
        return

    for i in range(2, n + 1 , 1):
        ary[i] = ary[i - 2] + ary[i - 1]


t = int(input())

for i in range(t):
    n = int(input())

    fibo(n)

    print(ary[n-1] , ary[n])