class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def expand_center(i,j):            
            while 0<=i<=j<n and s[i]==s[j]:
                i-=1
                j+=1                
            
            return (i+1, j)                
        
        res=max([expand_center(i,i+offset) for i in range(n) for offset in range(2)], key=lambda x: x[1]-x[0]+1)
        
        return s[res[0]:res[1]]