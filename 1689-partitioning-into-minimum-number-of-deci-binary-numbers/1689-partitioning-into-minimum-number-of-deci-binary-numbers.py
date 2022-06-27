class Solution:
    def minPartitions(self, n: str) -> int:
        maxi = 0
        i = 0
        while i <= len(n)//2:
            maxi = max(maxi, int(n[i]), int(n[-i-1]))
            if(maxi == 9):
                break
            i += 1
        return maxi