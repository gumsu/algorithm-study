n, l = map(int, input().split())
lights = []
for _ in range(n):
    lights.append(list(map(int, input().split())))

time = 0  # 시간
move = 0  # 이동한 거리
for i in range(n):
    b = lights[i][0] if i == 0 else lights[i][0] - lights[i-1][0]
    r = lights[i][1]
    g = lights[i][2]

    time += b
    move += b

    tmp_time = time % (r+g)  # 신호가 여러번 바뀐 시간을 뺀 시간 - 임시 변수
    if tmp_time < r:
        time += r-tmp_time

time += l-lights[n-1][0]

print(time)
