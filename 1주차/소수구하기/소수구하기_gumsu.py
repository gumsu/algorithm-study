m, n = map(int, input().split())

is_prime_number = [True for i in range(n+1)]

is_prime_number[0] = False
is_prime_number[1] = False

for i in range(2, n+1):
	if is_prime_number[i]:
		for j in range(i+i, n+1, i):
			is_prime_number[j] = False

for z in range(m, n+1):
	if is_prime_number[z]:
		print(z)