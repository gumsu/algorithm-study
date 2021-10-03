n, l = map(int, input().split())
lights = []
for _ in range(n):
    lights.append(list(map(int, input().split())))
# ------------------------
time = 0  # 시간

for i in range(n):
    b = lights[i][0] if i == 0 else lights[i][0]-lights[i-1][0]  # 전 신호등과의 사이거리
    r = lights[i][1]
    g = lights[i][2]

    time += b

    tmp_time = time % (r+g)  # 신호가 여러번 바뀐 시간을 뺀 시간 - 임시 변수
    if tmp_time < r:  # 아직 빨간 불이라서 기다려야 함
        time += r-tmp_time  # 기다려야 하는 시간 더하기

time += l-lights[n-1][0]

print(time)
