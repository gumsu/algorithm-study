arr = [0] * 10

for i in range(10):
	mushroom = int(input())
	
	if i == 0:
		arr[i] = mushroom
	else:
		arr[i] = arr[i-1] + mushroom

res = arr[0]

# print(*arr)
# print(res)

if res == 100:
	print(res)
else:
	for i in range(1, 10):
		if arr[i] >= 100 :
			if abs(arr[i] - 100) <= abs(arr[i-1] - 100):
				res = arr[i]
				break
			else:
				res = arr[i-1]
				break
		else:
			res = max(arr)
	print(res)