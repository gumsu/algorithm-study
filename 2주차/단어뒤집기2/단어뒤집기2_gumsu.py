s = input()

res = ""
tmp = ""
flag = False    # 태그라면 True 아니라면 False

for i in range(len(s)):

    if s[i] == "<":
        flag = True
        if tmp:         # 이미 tmp에 담겨 있는 것들이 있다면, 거꾸로 바꿔서 넣기
            res += tmp[::-1]
            tmp = ""
        tmp += s[i]

    elif s[i] == ">":
        flag = False
        tmp += s[i]
        res += tmp
        tmp = ""
    
    elif s[i] == " ":
        if flag:
            tmp += s[i]
        else:
            res += tmp[::-1] + ' '
            tmp = ""
    else:           # 영어, 한글, 숫자 등등
        tmp += s[i]

if tmp:
    res += tmp[::-1]
print(res)