a = int(input())
b = int(input())
c = int(input())

res = a * b * c
arr = [0] * 10

for i in str(res):
    arr[int(i)] += 1

for z in arr:
    print(z)