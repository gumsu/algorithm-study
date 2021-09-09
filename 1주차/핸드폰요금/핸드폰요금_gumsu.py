def young(x):
    temp = x // 30
    

    if (x % 30 >= 0):
        temp += 1

    price = temp * 10

    return price


def mins(x):
    temp = x // 60

    if (x % 60 >= 0):
        temp += 1

    price = temp * 15

    return price

n = int(input())
arr = list(map(int, input().split()))

young_price = 0
mins_price = 0

for i in arr:
    young_price += young(i)
    mins_price += mins(i)
  
if (young_price < mins_price):
    print(f'Y {young_price}')
elif (young_price > mins_price):
    print(f'M {mins_price}')
else:
    print(f'Y M {young_price}')