class Solution:
    
    def canBe(self, sides):
        stat1 = ((sides[0] + sides[1]) > sides[2])
        stat2 = ((sides[1] + sides[2]) > sides[0])
        stat3 = ((sides[0] + sides[2]) > sides[1])
        return stat1 and stat2 and stat3
    
    def adder(self, nums):
        if(self.canBe(nums)):
            return nums[0] + nums[1] + nums[2]
        else:
            return 0
        
    def largestPerimeter(self, nums: List[int]) -> int:
        if(len(nums) == 3):
            return self.adder(nums)
        else:
            p = 0
            nums = sorted(nums)
            for i in range(len(nums)-1, 1, -1):
                res = self.adder([nums[i-2], nums[i-1], nums[i]])
                if(res > p):
                    p = res
                

                
                
        return p
                