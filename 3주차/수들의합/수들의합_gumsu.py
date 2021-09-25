n = int(input())

maxNum = 1

while True:
	if n >= 0:
		n -= maxNum
		maxNum += 1
	else:
		print(maxNum -2)
		break