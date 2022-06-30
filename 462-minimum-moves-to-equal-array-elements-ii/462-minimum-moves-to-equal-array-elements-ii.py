class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        midInd = len(nums)//2
        mid = nums[midInd]
        moves = 0
        for num in nums:
            moves += abs(num-mid)
        return moves