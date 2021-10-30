n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int, input().split())))

time.sort(key= lambda x: (x[1], x[0]))

start, end = time.pop(0)
cnt = 1

for i in range(n-1):
    if time[i][0] >= end:
        start, end = time[i][0], time[i][1]
        cnt += 1

print(cnt)