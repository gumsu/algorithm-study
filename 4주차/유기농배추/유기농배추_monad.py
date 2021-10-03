import sys
sys.setrecursionlimit(10000)

t = int(input())


def dfs(y, x):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[y][x] == 0:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(y-1, x)
        dfs(y, x-1)
        dfs(y, x+1)
        dfs(y+1, x)
        return True
    return False


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(n):  # y
        for j in range(m):  # x
            if dfs(i, j):
                cnt += 1
    print(cnt)
