class Solution:
    def countVowelPermutation(self, n: int) -> int:
        m = [1,1,1,1,1]		
        for _ in range(n - 1): m = [m[1], m[0] + m[2], m[0] + m[1] + m[3] + m[4], m[2] + m[4], m[0]]            
        return sum(m) % 1000000007
