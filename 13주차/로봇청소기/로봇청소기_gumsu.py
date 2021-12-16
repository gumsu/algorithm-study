from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]
'''
1. 현재 위치 청소
2. 현재 방향에서 왼쪽 방향으로 돌리기
    a. 청소 가능하면 하기, 다시 1번부터
    b. 청소 못하면 회전
    c. 후진
    d. 멈춤
'''

n, m = map(int, input().split())

# d가 0 북 / 1 동 / 2 남 / 3 서
r, c, d = map(int, input().split())
# 0 빈칸 1 벽
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

cnt = 0

q = deque()
q.append((r, c))

while q:
    x, y = q.popleft()
    if board[x][y] == 0 and not visited[x][y]:
        visited[x][y] = True
        cnt += 1
    
    # 반시계 방향으로 회전하면서 확인, 청소
    for i in range(4):
        d = (d+3) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 < nx < n and 0 < ny < m and not visited[nx][ny] and board[nx][ny] == 0:
            visited[nx][ny] = True
            cnt += 1
            q.append((nx, ny))
            break
    
    # 후진 (방향은 그대로)
    else:
        nd = (d+2) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if nx < 0 or nx > n or ny < 0 or ny > m or board[nx][ny] == 1:
            break
        q.append((nx, ny))
    
# for z in visited:
#     print(z)
print(cnt)