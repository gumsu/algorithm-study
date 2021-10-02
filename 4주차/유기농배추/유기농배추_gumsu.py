import sys
sys.setrecursionlimit(50000)

def dfs(x, y):
    board[x][y] = 0
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < n and 0 <= b < m and board[a][b] == 1:
            dfs(a, b)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for i in range(n)]
    cnt = 0

    for j in range(k):
        a, b = map(int, input().split())
        board[b][a] = 1
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                dfs(i, j)
                cnt += 1
    
    print(cnt)