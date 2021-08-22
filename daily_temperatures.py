def dailyTemperatures(nums):
    res = [0] * len(nums)
    stack = [] 
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[i] >= nums[stack[-1]]:
            stack.pop() 
        if stack:
            res[i] = stack[-1] - i
        stack.append(i)
    return res    