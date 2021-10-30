from collections import deque
dy = [-1, 0, 1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
q = deque()

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and box[nx][ny][nz] == 0:
                box[nx][ny][nz] = box[x][y][z] + 1
                q.append((nx, ny, nz))

m, n, h = map(int, input().split())
box = []
# 1 익은 토마토 / 0 익지 않은 토마토 / -1 빈 칸
for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int, input().split())))
    box.append(tmp)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append((i, j, k))

bfs()
def result():
    res = 0
    for i in box:
        for j in i:
            for z in j:
                if z == 0:
                    return -1
                res = max(res, z)
    else:
        return res -1
print(result())