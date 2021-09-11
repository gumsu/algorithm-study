# boj 10804
cards = list(range(1, 21))

for i in range(10):
    x, y = map(int, input().split())
    s, e = x-1, y-1
    offset = e-s+1
    for j in range(offset//2):
        cards[s+j], cards[e-j] = cards[e-j], cards[s+j]

print(' '.join(map(str, cards)))
