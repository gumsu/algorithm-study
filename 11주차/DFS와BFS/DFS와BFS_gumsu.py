from collections import deque

def dfs(depth):
    print(depth, end=' ')
    visited[depth] = True

    for i in range(1, n+1):
        if not visited[i] and graph[depth][i]:
            dfs(i)

def bfs(depth):
    visited[depth] = False

    q = deque()
    q.append(depth)

    while q:
        x = q.popleft()
        print(x, end= ' ')
        for i in range(1, n+1):
            if visited[i] and graph[x][i]:
                visited[i] = False
                q.append(i)

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)