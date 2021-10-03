# 채점 왜이렇게 오래 걸려,,,
# 또 런타임 에러 ...

import sys
sys.setrecursionlimit(100000)

n = int(input())

graph = [[] for _ in range(n)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)
# -------------------------
parents = [0]*n
visited = [False]*n


def dfs(x):
    for i in graph[x-1]:
        if not visited[i-1]:
            parents[i-1] = x
            visited[i-1] = True
            dfs(i)


dfs(1)

for i in range(1, n):
    print(parents[i])

# 리스트 인덱스가 헷갈림
