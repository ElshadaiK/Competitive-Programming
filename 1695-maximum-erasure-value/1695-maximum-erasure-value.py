class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxScore = 0
        temp = set()
        total = 0
        left = 0
        right = 1
        temp.add(nums[0])
        total += nums[0]
        while(right < len(nums)):
            if(nums[right] not in temp):
                temp.add(nums[right])
                total += nums[right]
                maxScore = max(maxScore, total)
                right += 1
            else:
                while(nums[right] in temp):
                    if(nums[left] != nums[right]):
                        temp.remove(nums[left])
                        total -= nums[left]
                        left += 1
                    else:
                        left += 1
                        right += 1
                        break
            maxScore = max(maxScore, total)
        maxScore = max(maxScore, total)
        return maxScore