from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

'''
뱀의 모든 위치를 큐에 넣는다.
움직일떄마다 사과 확인 + 뱀 확인
- 뱀이면 끝
- 사과 있으면 큐에 (머리)넣기
- 사과 없으면 큐에서 (머리)넣고 (꼬리)빼기
방향 확인하여 현재 방향 바꿔주기
'''

if __name__ == "__main__":
    n = int(input())
    k = int(input())

    board = [[0]*n for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        a-=1
        b-=1
        board[a][b] = 1

    l = int(input())

    # now 현재 방향(0,1,2,3 순서) 
    now_direction = 1

    # 큐의 제일 앞 - 머리, 큐의 제일 뒤 - 꼬리
    q = deque()
    q.append((0, 0))
    board[0][0] = 2

    # 뱀의 길이
    length = 1
    # 게임이 몇 초에 끝나는 지
    cnt = 0

    snake = []
    times = []
    # l 왼 d 오
    # 게임 시작 x초가 끝난 뒤 90도 방향 회전
    for _ in range(l):
        x, c = map(str, input().split())
        x = int(x)
        snake.append([x, c])
        times.append(x)
    
    '''
    뱀은 계속 움직이고, x초에 c로 회전을 하는 것이다.
    move(x, c)는 x초만큼 간 후 c로 방향을 전환하는 방식으로 구현했기 떄문에
    현재 x초에서 이전 x초만큼 빼주는 코드를 구현해야 한다.
    입력받은 x, c 만큼 돌았어도 뱀이 죽지 않았다면 계속 움직이기 떄문에
    for-else 안에 n+1만큼 돌게 하여 무조건 벽에 박게 만든다.
    '''
    if l > 1:
        for i in range(1, l):
            snake[i][0] = times[i] - times[i-1]
    # print(snake)
    for x, c in snake:
        if move(x, c) == False:
            break
    else:
        move(n+1, 'D')
    print(cnt+1)


# time 시간 dir 움직이는 방향
def move(time, dir):
    global now_direction, cnt

    for _ in range(time):
        # print(q)
        # print(f'방향: {now_direction}')
        # print(cnt)
        # print('-----')
        # for z in board:
        #     print(z)
        # print('-----')

        x, y = q[0]
        if x < 0 or x >= n or y < 0 or y >= n :
            return False

        # 위
        if now_direction == 0:
            nx = x-1
            ny = y
            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                return False

            if is_snake(nx, ny):
                return False

            if is_apple(nx, ny):
                q.appendleft((nx,ny))
                board[nx][ny] = 2
            else:
                q.appendleft((nx, ny))
                tx, ty = q.pop()
                board[nx][ny] = 2
                board[tx][ty] = 0
            
            cnt += 1

        # 오
        elif now_direction == 1:
            nx = x
            ny = y+1

            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                return False
                
            if is_snake(nx, ny):
                return False

            if is_apple(nx, ny):
                q.appendleft((nx,ny))
                board[nx][ny] = 2
            else:
                q.appendleft((nx, ny))
                tx, ty = q.pop()
                board[nx][ny] = 2
                board[tx][ty] = 0
            
            cnt += 1

        # 아
        elif now_direction == 2:
            nx = x+1
            ny = y

            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                return False
                
            if is_snake(nx, ny):
                return False

            if is_apple(nx, ny):
                q.appendleft((nx,ny))
                board[nx][ny] = 2
            else:
                q.appendleft((nx, ny))
                tx, ty = q.pop()
                board[nx][ny] = 2
                board[tx][ty] = 0

            cnt += 1

        # 왼
        elif now_direction == 3:
            nx = x
            ny = y-1

            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                return False
                
            if is_snake(nx, ny):
                return False

            if is_apple(nx, ny):
                q.appendleft((nx,ny))
                board[nx][ny] = 2
            else:
                q.appendleft((nx, ny))
                tx, ty = q.pop()
                board[nx][ny] = 2
                board[tx][ty] = 0

            cnt += 1

    if dir == 'L':
        now_direction = (now_direction + 3) % 4    
    elif dir == 'D':
        now_direction = (now_direction + 1) % 4



def is_apple(x, y):
    if board[x][y] == 1 :
        return True
    else:
        return False

def is_snake(x, y):
    if board[x][y] == 2:
        return True
    else:
        return False