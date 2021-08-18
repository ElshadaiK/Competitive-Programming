class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        found = False
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    result.append(i)
                    result.append(j)
                    found = True
                    break
            if(found):
                break
        return result
                