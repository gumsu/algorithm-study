k, n = map(int, input().split())
lans = []
for _ in range(k):
    lans.append(int(input()))

start = 0
end = max(lans)
result = 0
while start <= end:
    l = (start+end)//2
    if l == 0:
        l = 1  # ZeroDivisionError 발생 방지
    total = 0
    for lan in lans:
        total += lan//l
    if total < n:
        end = l-1
    else:
        result = l
        start = l+1

print(result)

# 파라메트릭 서치
