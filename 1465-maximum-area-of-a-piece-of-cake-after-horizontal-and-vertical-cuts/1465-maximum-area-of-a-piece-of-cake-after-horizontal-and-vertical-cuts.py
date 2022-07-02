class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        hmax = 0
        vmax = 0
        for i in range(1, len(horizontalCuts)):
            hmax = max(hmax, horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            vmax = max(vmax, verticalCuts[i]-verticalCuts[i-1])
        return (vmax*hmax)%(10**9 + 7)
        