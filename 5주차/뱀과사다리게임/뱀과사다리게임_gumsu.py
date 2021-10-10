from collections import deque

def bfs():
    q = deque()
    q.append(1)
    checked[1] = True

    while q:
        now = q.popleft()

        for i in range(1, 7):
            move = now + i

            if 0 < move <= 100 and not checked[move]:
                if ladder[move] != 0:
                    move = ladder[move]
                
                if snake[move] != 0:
                    move = snake[move]
                
                if not checked[move]:
                    q.append(move)
                    checked[move] = True
                    board[move] = board[now] + 1

n, m = map(int, input().split())

ladder = [0]* 101
snake = [0]* 101

board = [0]* 101
checked = [False] * 101

for i in range(n):
    a, b = map(int, input().split())
    ladder[a] = b

for i in range(m):
    a, b = map(int, input().split())
    snake[a] = b

bfs()

print(board[100])