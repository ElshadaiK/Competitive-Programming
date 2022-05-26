class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        track = []
        
        def dfs(i):
            if i == len(nums):
                ans.append(track[:])  
            else:
                # choose num_i
                track.append(nums[i])
                dfs(i+1)
                track.pop()
                
                # not choose num_i
                dfs(i+1)
                
        dfs(0)
        
        return ans