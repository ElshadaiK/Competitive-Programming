def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    colors = [0]*3
    for i in nums:
        colors[i] += 1
        
    k = 0
    for i in range(len(colors)):
        for j in range(colors[i]):
            nums[k] = i
            k += 1
        