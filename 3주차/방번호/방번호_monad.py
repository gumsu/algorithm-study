# boj 1475 방번호
# 구현

import math

nums = input()
used = [0] * 10

for num in nums:
    num = int(num)
    used[num] += 1

used[6], used[9] = math.ceil((used[6]+used[9])/2), 0

print(max(used))

# 내가 이상한 방법으로 한 건 아닌지 확인 필요..
# used 라는 카드 사용여부 리스트를 만들어 해당 숫자의 자리에 +1 처리
# 6,9는 같은 카드가 2개 있는것으로 간주하므로 2개의 개수를 2로 나눔
# used중의 최대값을 출력
