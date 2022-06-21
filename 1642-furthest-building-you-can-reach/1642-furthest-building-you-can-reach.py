class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        idx = 0
        h = []
        while idx < len(heights) - 1:
            diff = heights[idx + 1] - heights[idx]
            if diff <= 0:
                pass
            elif diff <= bricks:
                heapq.heappush(h, -diff)
                bricks -= diff
            elif ladders > 0:                
                heapq.heappush(h, -diff)
                max_bricks = -heapq.heappop(h)
                ladders -= 1
                bricks += max_bricks - diff
            else:
                break
                
            idx += 1                
            
        return idx