k = int(input())
tree = list(map(int, input().split()))
level = [[]for _ in range(k)]

def inorder(tree, depth):
    if depth == k:
        return
    mid = len(tree) // 2
    level[depth].append(tree[mid])
    inorder(tree[:mid], depth+1)
    inorder(tree[mid+1:], depth+1)

inorder(tree, 0)

for i in level:
    print(*i)