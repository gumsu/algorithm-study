n = int(input())
lines = []

for _ in range(n):
    x, y = map(int, input().split())
    if lines:
        last_line = lines[-1]
        if x <= last_line[1]:
            if y > last_line[1]:
                last_line[1] = y
        else:
            lines.append([x, y])
    else:
        lines.append([x, y])

total = 0
for line in lines:
    total += (line[1] - line[0])

print(total)
