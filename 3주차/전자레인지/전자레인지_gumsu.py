t = int(input())

a = 5 * 60  # 300
b = 1 * 60  # 60
c = 10

cnt1 = 0
cnt2 = 0
cnt3 = 0

if t % 10 != 0:
    print(-1)
else:
    while t > 0:
        if t >= a:
            cnt1 += t // a
            t %= a
        elif t >= b:
            cnt2 += t // b
            t %= b
        elif t >= c:
            cnt3 += t // c
            t %= c
        else:
            t += 1
            break

    print(cnt1, cnt2, cnt3)