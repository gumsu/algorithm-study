document = input()
word = input()
cnt = 0

while True:
    idx = document.find(word) # 처음 나오는 위치 반환
    if idx == -1:
        break

    cnt += 1
    document = document[idx + len(word): ]

print(cnt)