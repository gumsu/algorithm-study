from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1]*(n+1)
visited[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next in graph[now]:
        if visited[next] == -1:
            q.append(next)
            visited[next] = visited[now]+1

exist = False
for i in range(1, n+1):
    if visited[i] == k:
        print(i)
        exist = True

if exist == False:
    print(-1)
