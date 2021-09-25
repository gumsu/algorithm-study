# boj 2563 색종이
# 구현, 완전탐색

paper = [[0]*100 for _ in range(100)]  # 100*100 2차원배열

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            paper[j][k] = 1

area = 0
for i in range(100):
    area += sum(paper[i])

print(area)


# 100*100 배열을 만들어 붙여진 곳을 1 표시하면 되는데
# 중복되는 부분을 어떻게 처리할지만 생각하다보니 어렵게 풀게 됨

# -------------------------------------오답-----------------------------------------
# n = int(input())
# lx = [0]*n
# ly = [0]*n
# for i in range(n):
#     lx[i], ly[i] = map(int, input().split())

# area = 100*n

# for i in range(n):
#     x = lx[i]
#     y = ly[i]

#     for j in range(i+1, n):
#         cx = lx[j]
#         cy = ly[j]
#         if ((cx <= x and x <= cx+10) or (cx <= x+10 and x <= cx)) and ((cy <= y and y <= cy+10) or (cy <= y+10 and y <= cy)):
#             # 색종이 겹치는 경우
#             if x < cx:
#                 width = x+10-cx
#             else:
#                 width = cx+10-x
#             if y < cy:
#                 height = y+10-cy
#             else:
#                 height = cy+10-y

#             area -= width*height

# print(area)
