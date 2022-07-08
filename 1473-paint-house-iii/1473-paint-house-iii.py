class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
            @cache
            def dp(i, nbr, prev_color):
                # i th house, remian target, previous color
                if i == m:
                    if nbr == 0:
                        return 0
                    else:
                        return float('inf')

                if m - i < nbr or nbr < 0:
                    # prune, case 1 not enough house to make up to target
                    # case 2, too much nbr
                    return float('inf')  

                res = float('inf')

                if houses[i] == 0:
                    # need paint
                    for color in range(1, n+1):
                        res = min(res, dp(i+1, nbr - (color != prev_color), color) + cost[i][color-1])    
                else:
                    res = dp(i+1, nbr - (houses[i] != prev_color), houses[i])

                return res

            ans = dp(0, target, -1)

            return ans if ans != float('inf') else -1