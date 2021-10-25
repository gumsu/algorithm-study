# 시간 초과..

n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

total = 10000000000  # 합의 절대값
result = [0]*3  # 용액 결과값

for i in range(n-2):
    # i가 p1
    start = i+1  # p2
    end = n-1  # p3

    while (start < end):
        # 합의 절대값 (임시)
        tmp_total = solutions[i]+solutions[start]+solutions[end]
        if abs(tmp_total) < abs(total):
            total = tmp_total
            result[0] = solutions[i]
            result[1] = solutions[start]
            result[2] = solutions[end]

        if tmp_total > 0:
            end -= 1
        elif tmp_total < 0:
            start += 1
        elif tmp_total == 0:
            break

print(' '.join(map(str, result)))
