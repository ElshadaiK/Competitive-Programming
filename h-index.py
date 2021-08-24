class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lst=[0]*(len(citations)+1)
        for i in citations:
            if i>=len(citations)+1:
                lst[-1]+=1
            else:
                lst[i]+=1
        sm=0
        for i in range(len(lst)-1,-1,-1):
            sm+=lst[i]
            if sm>=i:
                return i