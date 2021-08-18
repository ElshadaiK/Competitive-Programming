class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        for i in range(len(nums)):
            index = nums[i]
            result[i] = nums[index]
        return result