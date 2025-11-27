a = int(input())
b = int(input())

print(a*(b - int(b/10)*10))
print(a*(int(b/10) - int(b/100)*10))
print(a*(int(b/100)))
print(a*b)