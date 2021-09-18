n = int(input())

# ord 'a' = 97
# ord 'z' = 122
cnt = 0

for i in range(n):
    alpha = [0] * 123
    word = input()
    
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            if alpha[ord(word[j+1])] == 1:
                break
            alpha[ord(word[j])] = 1
    else:
        cnt += 1

print(cnt)