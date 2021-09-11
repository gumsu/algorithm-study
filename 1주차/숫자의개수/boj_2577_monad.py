# boj 2577

a = int(input())
b = int(input())
c = int(input())

abc = str(a*b*c)

for i in range(10):
    print(len(list(filter(lambda x: x == str(i), abc))))
