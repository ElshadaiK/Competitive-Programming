class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest, cur_longest = 0, min(1, len(nums))
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] : continue
            if nums[i] == nums[i - 1] + 1: cur_longest += 1
            else: longest, cur_longest = max(longest, cur_longest), 1
        return max(longest, cur_longest)