n = int(input())
people = list(map(int, input().split()))
res = [0]*n

for i in range(1, n+1):
    tmp = people[i-1]
    cnt = 0
    for j in range(n):
        if cnt == tmp and res[j] == 0:
            res[j] = i
            break
        elif res[j] == 0:
            cnt += 1
print(*res)