t = int(input())

for i in range(t):
    res = list()

    n = int(input())
    alpha = list(map(str, input().split()))
    
    for j in alpha:
        if not res:
            res.append(j)
        elif res[0] >= j:
            res.insert(0, j)
        else:
            res.append(j)
    print(''.join(res))