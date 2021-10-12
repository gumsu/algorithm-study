import sys

t = int(input())
INF = sys.maxsize

for _ in range(t):
    n = int(input())    # 편의점 개수
    board = [list(map(int, input().split())) for _ in range(n+2)]
    dis = [[INF] *(n+2) for _ in range(n+2)]

    for i in range(n+2):
        for j in range(n+2):
            if i == j :
                continue
            if abs(board[i][0] - board[j][0]) + abs(board[i][1] - board[j][1]) <= 1000:
                dis[i][j] = 1
    
    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
    
    if 0 < dis[0][n+1] < INF:
        print("happy")
    else:
        print("sad")