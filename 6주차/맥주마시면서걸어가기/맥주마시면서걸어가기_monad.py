# 오류..

from collections import deque

t = int(input())
locs = []
for _ in range(t):
    n = int(input())
    for _ in range(n+2):
        locs.append(list(map(int, input().split())))

    limit = 1000
    happy = True
    q = deque(locs[0])
    while q:
        now = q.popleft()
        for next in locs[1:]:
            if next[0]+next[1]-now[1]-now[0] <= 1000:
                q.append(next)
            else:
                happy = False

    if happy:
        print("happy")
    else:
        print("sad")
