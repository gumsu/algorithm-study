n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

lo = 1
hi = houses[n-1]-houses[0]
result = 0


def possible(dist):
    cnt = 1
    global c

    prev = houses[0]
    for i in range(n):
        if houses[i] - prev >= dist:
            cnt += 1
            prev = houses[i]
    if c <= cnt:
        return True
    return False


while (lo <= hi):
    mid = (lo+hi)//2
    if possible(mid):
        result = max(mid, result)
        lo = mid+1
    else:
        hi = mid - 1

print(result)
