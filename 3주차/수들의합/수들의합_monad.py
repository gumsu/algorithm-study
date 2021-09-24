# boj 1789 수들의 합
# 그리디

s = int(input())

n = 0
tmp = 0  # s를 테스트할 변수

for i in range(1, s+1):     # 1부터 차례대로 더해보다가,
    tmp += i
    n += 1
    if tmp > s:             # tmp가 s보다 커지면 n에서 1을 빼고 끝냄
        n -= 1              # 앞에서 나온 자연수 중 하나만 빼주면 되는 것이므로
        break

print(n)
