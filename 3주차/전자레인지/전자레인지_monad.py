# boj 10162 전자레인지
# 그리디

t = int(input())

buttons = [300, 60, 10]
result = []
for button in buttons:
    result.append(t//button)
    t %= button

if t != 0:
    print(-1)
else:
    print(' '.join(map(str, result)))
