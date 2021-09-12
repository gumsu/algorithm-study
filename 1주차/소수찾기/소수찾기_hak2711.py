from math import sqrt

n = int(input())
nums = list(map(int, input().split(' ')))


def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if(n % i == 0):
            return False
    return True


answer = 0

for num in nums:
    if isPrime(num) and (num != 1):
        answer += 1

print(answer)
