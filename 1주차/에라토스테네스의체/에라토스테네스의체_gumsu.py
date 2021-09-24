n, k = map(int, input().split())

is_prime_number = [True for i in range(n+1)]

cnt = 0

for i in range(2, n+1):
	for j in range(i, n+1, i):
		if is_prime_number[j]:
			is_prime_number[j] = False
			cnt += 1

			if cnt == k:
				print(j)
				break