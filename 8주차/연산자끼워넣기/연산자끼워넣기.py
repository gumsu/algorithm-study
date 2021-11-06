from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
# + - * /
operator_num = list(map(int, input().split()))

min_num = 1e9
max_num = -1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global max_num, min_num
    if depth == n:
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return
    
    if plus:
        dfs(depth+1, total+num[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total-num[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total*num[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total/num[depth]), plus, minus, multiply, divide-1)

dfs(1, num[0], operator_num[0], operator_num[1], operator_num[2], operator_num[3])

print(max_num)
print(min_num)