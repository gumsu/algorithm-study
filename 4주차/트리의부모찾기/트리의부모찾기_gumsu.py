import sys
sys.setrecursionlimit(10**8)

def dfs(num):
    for i in tree[num]:
        if not visited[i]:
            parent[i] = num
            visited[i] = True
            dfs(i)

n = int(input())

tree = [[] for i in range(n+1)]
parent = [0] * (n+1)
visited = [False] * (n+1)

for i in range(n-1):
    a, b = map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)

dfs(1)

for i in range(2, len(parent)):
    print(parent[i])