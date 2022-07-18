class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n,m = len(matrix),len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        
        # make prefix sum for every row
        for i in range(n):
            for j in range(m):
                dp[i][j] = matrix[i][j] + (dp[i][j-1] if j-1>=0 else 0)
        # print(*dp,sep="\n")        
        ans = 0
        # for every column see row sum
        for i in range(m):
            for j in range(i,m):
                d = {0:1}
                s = 0
                for r in range(n):
                    s += dp[r][j] - (dp[r][i-1] if i-1>=0 else 0)
                    if s-target in d:
                        ans += d[s-target] 
                        
                    if s in d:
                        d[s] += 1
                    else:
                        d[s] = 1
                        
        return ans