k = int(input())
op = list(input().split())
check = [False]*10
min_num = ""
max_num = ""

def available(i, j, k):
    if k == "<":
        return i < j
    else:
        return i > j

def dfs(depth, num):
    global min_num, max_num

    if depth == k+1:
        if min_num == "":
            min_num = num
        else:
            max_num = num
        return

    for i in range(10):
        if not check[i]:
            if depth == 0 or available(num[-1], str(i), op[depth-1]):
                check[i] = True
                dfs(depth+1, num+str(i))
                check[i] = False

dfs(0, "")

print(max_num)
print(min_num)