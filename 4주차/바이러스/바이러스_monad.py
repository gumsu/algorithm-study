c = int(input())
n = int(input())

graph = [[] for _ in range(c)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

visited = [False] * c
cnt = 0


def dfs(x):
    global cnt
    for i in graph[x-1]:
        if not visited[i-1]:
            cnt += 1
            visited[i-1] = True
            dfs(i)


dfs(1)
print(cnt-1)
