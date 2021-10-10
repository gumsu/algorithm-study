k, n = map(int, input().split())

cable = [int(input()) for _ in range(k)]

lt = 1
rt = max(cable)
longest = 0

while lt <= rt:
    cnt = 0
    mid = (lt + rt) // 2
    
    for x in cable:
        cnt += x // mid
        
    if cnt >= n:
        longest = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(longest)