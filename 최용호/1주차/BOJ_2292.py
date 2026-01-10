n = int(input())

layer = 1
max = 1

while n > max :
    max += 6 * layer
    layer += 1
    
print(layer)