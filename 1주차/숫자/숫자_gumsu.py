a, b = map(int, input().split())

if (a > b):
    a, b = b, a
    
count = b - a - 1

if (a == b):
    count = 0
    
arr = []
for i in range(a+1, b):
    arr.append(i)

print(count)
print(*arr)