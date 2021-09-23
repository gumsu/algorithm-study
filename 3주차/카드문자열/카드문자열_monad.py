# boj 13417 카드 문자열
# 그리디

import sys

t = int(sys.stdin.readline())               # 테스트 케이스 t 입력
for i in range(t):
    n = int(sys.stdin.readline())           # 카드 개수 n 입력
    cards = sys.stdin.readline().split()    # 알파벳 카드들 입력

    fronts = []                             # 첫번째 카드를 포함한 앞의 배열 (reversed)
    behinds = []                            # 첫번째 카드 뒤의 배열

    fronts.append(cards.pop(0))             # 첫번째 카드는 가장 앞에 가져오기
    while cards:                            # cards가 빈 리스트 될 때까지 반복
        if fronts[-1] >= cards[0]:          # 가장 앞의 알파벳보다 작거나 같으면 앞으로 보내기
            fronts.append(cards.pop(0))
        else:                               # 가장 앞의 알파벳보다 크면 뒤로 보내기
            behinds.append(cards.pop(0))
    fronts.reverse()
    print(''.join(fronts) + ''.join(behinds))


# 표준입력 **
