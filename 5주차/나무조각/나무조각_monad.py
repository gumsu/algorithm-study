nums = list(map(int, input().split()))
sorted_nums = sorted(nums)

while nums != sorted_nums:
    for i in range(4):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            print(' '.join(map(str, nums)))
