class Solution:
    def search(self, nums: List[int], target: int, point = 0) -> int:
        if(len(nums) > 1):
            index = (len(nums)-1) // 2
            print(point, index, nums)
            if(target == nums[index]):
                return index + point
            elif(target < nums[index]):
                return self.search(nums[:index+1], target, point)
            else:
                point += index+1
                return self.search(nums[index+1:], target, point)
        else:
            if(target == nums[0]):
                return point
            else:
                return -1