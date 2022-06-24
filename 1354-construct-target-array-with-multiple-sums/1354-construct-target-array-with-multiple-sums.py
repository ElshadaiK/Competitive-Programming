class Solution:
    def isPossible(self, target: List[int]) -> bool:
        h = []
        if len(target) == 1:
            return target[0] == 1
        total = sum(target)
        for e in target:
            heappush(h, -e)
        while True:
            e = -heappop(h)
            if e == 1: return True
            
            r = total - e
            if r == 1: return True
            
            nexte = e % r
            if nexte == 0 or e == nexte: return False
            
            e = nexte
            heappush(h, -e)
            total = e + r