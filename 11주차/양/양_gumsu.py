from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
total_sheep = 0
total_wolf = 0

# . 필드 # 울타리 o 양 v 늑대
# for z in graph:
#     print(z)

def bfs(a, b):
    global total_sheep, total_wolf
    wolf = 0
    sheep = 0
    visited[a][b] = True

    if graph[a][b] == 'o':
        sheep += 1
    elif graph[a][b] == 'v':
        wolf += 1

    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] != '#':
                if graph[nx][ny] == 'o':
                    sheep += 1
                elif graph[nx][ny] == 'v':
                    wolf += 1

                visited[nx][ny] = True
                q.append((nx,ny))
    if wolf >= sheep:
        total_wolf += wolf
    else:
        total_sheep += sheep

for i in range(r):
    for j in range(c):
        if graph[i][j] != '#' and not visited[i][j]:
            bfs(i, j)
print(total_sheep, total_wolf)