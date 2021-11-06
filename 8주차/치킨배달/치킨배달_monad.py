# 틀림
from itertools import combinations

n, m = map(int, input().split())
graph = []
chickens = []
houses = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            chickens.append([i, j])
        if graph[i][j] == 1:
            houses.append([i, j])

chick_distances = []
for m_chickens in combinations(chickens, m):
    chick_dist = 0
    for house in houses:
        dists = []
        for chicken in m_chickens:
            dists.append(abs(chicken[0]-house[0]) + abs(chicken[1]-chicken[1]))
        chick_dist += min(dists)
    chick_distances.append(chick_dist)

print(min(chick_distances))
