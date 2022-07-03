class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        f = 1
        d = 1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                f = d+1
            elif nums[i] < nums[i-1]:
                d = f+1
        res = min(len(nums) , max(f, d))
        return res