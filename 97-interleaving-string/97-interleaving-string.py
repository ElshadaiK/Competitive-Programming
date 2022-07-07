class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1) + 2, len(s2) + 2
        if n + m - 4 != len(s3): return False
        dp = [0] * m
        dp[1] = 1
        for i in range(1, n):
            for j in range(1, m):
                up = dp[j] and (i < 2 or s1[i-2] == s3[j+i-3])
                left = dp[j-1] and (j < 2 or s2[j-2] == s3[j+i-3])
                dp[j] = up or left
        return dp[-1]