s = input()
arr = list(s)

# a = 97
alpha = [0]*26
for i in range(len(arr)):
    j = ord(arr[i]) - 97
    alpha[j] += 1

cnt = 0

def dfs(depth, num):
    global cnt

    if depth == len(arr):
        cnt += 1
        return
    
    for i in range(26):
        if not alpha[i] or num == i:
            continue
        alpha[i] -= 1
        dfs(depth+1, i)
        alpha[i] += 1
        
dfs(0, -1)
print(cnt)