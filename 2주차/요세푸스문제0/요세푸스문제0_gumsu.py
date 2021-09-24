n, k = map(int, input().split())
arr = list(range(1, n+1))
res = []
num = 0
while arr:
    num += k-1
    if num >= len(arr):
        num %= len(arr)
    res.append(arr.pop(num))

print('<'+', '.join(map(str, res)) +'>')