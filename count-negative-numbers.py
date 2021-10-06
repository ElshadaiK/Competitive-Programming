class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            rows = len(grid[i]) - 1
            mini_count = rows
            for j in range(rows+1):
                if(grid[i][j] >= 0):
                    j = (rows +  j)//2
                else:
                    mini_count = j-1
                    break
            if(mini_count == 0):
                count += rows
            else:
                count += rows-mini_count
                    
        return count