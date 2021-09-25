n = input()

num = [0] * 10

for i in n:
	num[int(i)] += 1

tmp = num[6] + num[9]
if (tmp % 2 == 0) :
	num[6] = num[9] = tmp // 2
else :
	num[6] = num[9] = tmp // 2 + 1

print(max(num))