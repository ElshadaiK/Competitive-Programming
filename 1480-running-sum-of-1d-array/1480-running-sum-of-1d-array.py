class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0]
        for num in nums:
            res.append(res[-1] + num)
        return res[1:]
        