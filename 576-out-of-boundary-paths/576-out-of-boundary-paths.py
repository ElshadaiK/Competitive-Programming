class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = int(1e9+7)
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        
        @cache
        def rec(row, col, moves):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1
            if moves == 0:
                return 0
            ret = 0
            for dr, dc in dirs:
                ret += rec(row+dr, col+dc, moves-1)
                ret %= MOD
            return ret
        
        return rec(startRow, startColumn, maxMove)