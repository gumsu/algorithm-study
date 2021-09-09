n = int(input())
arr = list(map(int, input().split()))
is_prime = [True for i in range(1001)]
is_prime[0] = False
is_prime[1] = False
cnt = 0

for i in range(2, 1001):
    for j in range(i+i, 1001, i):
            if is_prime[i]:
                is_prime[j] = False

for z in arr:
    if is_prime[z]:
        cnt += 1

print(cnt)