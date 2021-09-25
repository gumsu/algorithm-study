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


# 전형적인 그리디 문제
# 마지막 회차에 10으로 나누어떨어지지 않으면 -1 출력
