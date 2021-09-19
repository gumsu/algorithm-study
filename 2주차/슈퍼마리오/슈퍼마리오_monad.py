# boj 2851 ### 런타임 에러

mushrooms = []
for i in range(10):
    mushrooms.append(int(input()))

score = 0
i = 0
while i < 10:
    score += mushrooms[i]
    if score >= 100:
        break
    i += 1

if (score-100) > (100-(score-mushrooms[i])):
    score = score-mushrooms[i]

print(score)
