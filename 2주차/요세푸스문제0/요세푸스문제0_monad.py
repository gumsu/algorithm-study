# boj 11866

n, k = map(int, input().split())
arr = list(range(1, n+1))

result = []
d_point = k-1

while len(arr) > 0:
    while d_point >= len(arr):
        d_point -= len(arr)
    result.append(arr.pop(d_point))
    d_point = d_point+k-1

print("<"+", ".join(map(str, result))+">")
