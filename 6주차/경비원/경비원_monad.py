m, n = map(int, input().split())
k = int(input())
inputs = []
for _ in range(k+1):
    dir, dist = map(int, input().split())
    if dir == 1:
        inputs.append(dist)
    if dir == 2:
        inputs.append(m+n+m-dist)
    if dir == 3:
        inputs.append(m+m+n+n-dist)
    if dir == 4:
        inputs.append(m+dist)
loc = inputs[-1]

total_length = (n+m)*2
total = 0
for store in inputs:
    total += min(abs(store-loc), total_length-abs(store-loc))

print(total)
