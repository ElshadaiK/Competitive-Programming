class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        # it has to be 1 
        # dfs to all 8 directions
        # dp can be used
        m = len(mat)
        n = len(mat[m-1])
        self.dxn = [(1,0), (0,1), (1,1), (1,-1)]
        
        maximumLine = 0
        dp = dict()
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] == 1:
                    dp[(i, j)] = [1] * 4
                    maximumLine = max(maximumLine, self.dfs(i,j,mat,dp,m,n))
        return maximumLine
        
        
    def dfs(self, row, col, mat, dp, m, n):
        count = 1
        for ind, (x, y) in enumerate(self.dxn):
            old_row = x + row
            old_col = y + col
            if(self.isValid(old_row, old_col, mat, m, n)):
                dp[(row, col)][ind] += dp[(old_row, old_col)][ind]
                count = max(count, dp[(row, col)][ind])
        return count

                 
        
    def isValid(self, row, column, matrix, m, n):
        return (
            0 <= row < m and 
            0 <= column < n and
            matrix[row][column] == 1
        )
    
    
        