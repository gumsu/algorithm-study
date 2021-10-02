n, k = map(int,input().split())
country = []

for i in range(n):
    tmp = list(map(int, input().split()))
    country.append(tmp)

country.sort(key=lambda x: (-x[1], -x[2], -x[3]))

cnt = 1

for i in range(n):
    if k == country[i][0]:
        num = i

# print(num)  # 현재 등수를 구하기 원하는 나라의 위치

for i in range(n):
    if country[num][1:] == country[i][1:]:
        break
    cnt +=1


print(cnt)

# for z in country:
#     print(z)