# boj 1748
import math

n = int(input())
d = int(math.log10(n)) + 1  # n의자릿수

result = 0
for i in range(1, d):  # n의자릿수보다 1자리 작은 단위까지만 for문
    result += (10**(i-1))*9*i

result += (n-(10**(d-1))+1)*d

print(result)
