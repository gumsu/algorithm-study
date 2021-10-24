from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1]*(n+1)
distance[x] = 0

q = deque([x])
while q:  # q가 남아있는 동안 지속
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == -1:  # 방문 안한 노드
            q.append(next)
            distance[next] = distance[now]+1

exist = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        exist = True

if exist == False:
    print(-1)
