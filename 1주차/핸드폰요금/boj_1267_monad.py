# boj 1267

n = int(input())
c_mins = list(map(int, input().split()))

y_fee = 0
m_fee = 0
for i in range(n):
    y_fee += (c_mins[i]//30 + 1)*10
    m_fee += (c_mins[i]//60 + 1)*15

if y_fee < m_fee:
    print('Y', end=' ')
elif y_fee == m_fee:
    print('Y M', end=' ')
else:
    print('M', end=' ')

print(min(y_fee, m_fee))
