n = input()

n_len = len(n) - 1
res = 0
i = 0

while i < n_len :
	res += 9 * (10 ** i) * (i + 1)
	i += 1

res += ((int(n) - (10 ** n_len)) + 1) * (n_len + 1)
print(res)

# 1의 자리수 ~ 9 * 1
# 10의 자리수 90 * 2
# 100의 자리수 900 * 3
# 1000의 자리수 9000 * 4 ....