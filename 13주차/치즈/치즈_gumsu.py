from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

'''
처음에 모든 지점을 탐색해서 외부 공간, 내부 공간을 확인하여 체크
녹는 치즈를 확인
녹은 치즈를 빈 공간으로 바꿔주기
위에  반복
'''

# 0,0 좌표는 무조건 외부 공간 -> 0,0 좌표와 연결되어 있는지 탐색
def search_space(a, b):
    _checked = [[False]*m for _ in range(n)]
    _checked[a][b] = True

    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not _checked[nx][ny] and board[nx][ny] == 0:
                _checked[nx][ny] = True
                q.append((nx, ny))
    
    return _checked

def melting_cheese(x, y):
    cnt = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and checked[nx][ny] and board[nx][ny] == 0:
            cnt += 1
    
    if cnt >= 2:
        c.append((x, y))

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

while True:
    # True = 외부공간 , False = 내부공간 or 치즈공간
    checked = search_space(0,0)

    c =[]
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                melting_cheese(i, j)

    if not c:
        break

    cnt += 1

    for a, b in c:
        board[a][b] = 0
        checked[a][b] = True

print(cnt)    
# for z in checked:
#     print(z)

# for z in board:
#     print(z)

'''
8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0
'''