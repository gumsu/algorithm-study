# BOJ 10093
# 두 양의 정수가 주어졌을 때, 두 수 사이에 있는 정수를 모두 출력하는 프로그램을 작성하시오.

x, y = map(int, input().split())

a = min(x, y)
b = max(x, y)

if (a == b):
    n = 0
else:
    n = b-a-1
print(n)

for i in range(a+1, b):
    print(i, end=' ')
