class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [0] * len(ratings)
        h = [(r, i) for i, r in enumerate(ratings)]
        heapify(h)
        res = 0
		
        while h:
            r, idx = heappop(h)
            x = y = 1
            if idx - 1 >= 0 and r > ratings[idx - 1]:
                x = candies[idx - 1] + 1
            if idx + 1 < len(ratings) and r > ratings[idx + 1]:
                y = candies[idx + 1] + 1
            candies[idx] = max(x, y)
            res += candies[idx]
			
        return res
