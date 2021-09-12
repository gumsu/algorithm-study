from math import sqrt

m, n = map(int, input().split())


def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if(n % i == 0):
            return False
    return True


for i in range(m, n+1):
    if (isPrime(i)) and i != 1:
        print(i)
