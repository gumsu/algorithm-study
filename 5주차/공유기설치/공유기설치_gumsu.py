n, c = map(int, input().split())
house = []
for _ in range(n):
    tmp = int(input())
    house.append(tmp)

house.sort()

# 배치할 수 있는 공유기의 개수 리턴
def Count(length):
    cnt = 1
    end_point = house[0]
    for i in range(1, n):
        # 마지막에 배치한 지점과 현재 내가 배치하려고 하는 집의 거리 계산
        if house[i]-end_point >= length:
            cnt += 1
            end_point = house[i]
    return cnt
            
lt, rt = 1, max(house)

while lt <= rt:
    mid = (lt + rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid+1
    else:   # 원하는 만큼 배치 못했으므로 rt 값을 줄여 범위를 좁힌다.
        rt = mid-1
print(res)