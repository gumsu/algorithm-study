arr = range(21)

for i in range(10):
    a, b = map(int, input().split())
    tmp = arr[a:b+1][::-1]

    arr = [*arr[:a], *tmp, *arr[b+1:]]

arr.pop(0)
print(*arr)