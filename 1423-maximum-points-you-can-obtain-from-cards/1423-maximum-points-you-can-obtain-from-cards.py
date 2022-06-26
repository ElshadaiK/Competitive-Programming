class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if(k == len(cardPoints)):
            return sum(cardPoints)
        start = 0
        total = sum(cardPoints[:k])
        maximum = total 
        i = 1
        while(i <= k):
            total += cardPoints[-i] - cardPoints[k-i]
            maximum = max(total, maximum)
            i += 1
        maximum = max(total, maximum)
        return maximum
        