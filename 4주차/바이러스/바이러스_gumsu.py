def dfs(num):
    global cnt

    for i in graph[num]:
        if not visited[i]:
            cnt += 1
            visited[i] = True
            dfs(i)

node = int(input())
edge = int(input())
visited = [False] * (node+1)
cnt = 0

graph = [[] for i in range(node+1)]

for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

print(cnt-1)