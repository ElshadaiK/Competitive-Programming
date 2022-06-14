class Solution:       
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1)>len(word2):
            word2,word1=word1,word2        
        
        m,n=len(word1),len(word2)
        prev=[0] * (m+1)
        
        for i in range(n-1, -1, -1):
            curr=[0] * (m+1)
            for j in range(m-1, -1, -1):
                if word1[j] == word2[i]:
                    curr[j]=1 + prev[j+1]
                else:
                    curr[j]=max(curr[j+1], prev[j])
            prev=curr
        return m + n - 2*prev[0]