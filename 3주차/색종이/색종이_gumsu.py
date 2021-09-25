n = int(input())


arr = [[0]*100 for i in range(100)]

for i in range(n):
    x, y = map(int, input().split())
    
    for j in range(10):
        for k in range(10):
            arr[x+j][y+k] += 1

overlap = 0
for z in arr:
    overlap += z.count(0)

# 총 면적 10000 에서 면적이 0인 부분 제거 (색종이 부분이 아닌 곳)
print(10000 - overlap)