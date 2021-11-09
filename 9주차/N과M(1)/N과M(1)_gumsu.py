def DFS(x, res, check):
    if x == m:
        print(res)
        return
    for i in range(1, n+1):
        if not check[i]:
            check[i] = True
            DFS(x+1, res + str(i) + ' ', check)
            check[i] = False

if __name__ == "__main__":
    n, m = map(int, input().split())
    check = [False for _ in range(n+1)]
    res = ''
    DFS(0, res, check)