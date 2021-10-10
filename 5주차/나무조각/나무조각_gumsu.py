wood = list(map(int, input().split()))

sorted_wood = list(range(1,6))

while wood != sorted_wood:
    for i in range(4):
        if wood[i] > wood[i+1]:
            wood[i], wood[i+1] = wood[i+1], wood[i]
            print(*wood)