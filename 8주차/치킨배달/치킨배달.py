from itertools import combinations

n, m = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
home, chicken = [], []

# 1 집 2 치킨집
# 집과 치킨집 좌표 구하기
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append((i,j))
        elif board[i][j] == 2:
            chicken.append((i,j))

all_dist = []

# 치킨집 중에서 m개 고른 조합 리스트
for selected_chicken in combinations(chicken, m):
    res = 0
    for y in home:
        distance = 100
        for x in selected_chicken:
            tmp = abs(x[0]-y[0])+abs(x[1]-y[1])
            distance = min(distance, tmp)
        # 모든 집의 치킨 거리의 합
        res += distance
    all_dist.append(res)

# print(home)
# print(chicken)
# print(all_dist)
print(min(all_dist))