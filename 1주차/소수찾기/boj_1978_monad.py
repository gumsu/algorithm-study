# boj 1978 -- 2도 소수임
import math


def isPrime(num):
    if num <= 1:
        return False
    if num != 2 and num % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True


n = int(input())
nums = list(map(int, input().split()))

print(len(list(filter(isPrime, nums))))
