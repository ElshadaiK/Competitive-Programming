class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # don't sort
        heap = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if(diff > 0):
                if ladders > 0:
                    ladders -= 1
                    heapq.heappush(heap, diff)
                else:
                    if len(heap) > 0 and heap[0] < diff and heap[0] <= bricks:
                        heapq.heappush(heap, diff)
                        minHeight = heapq.heappop(heap)
                        bricks -= minHeight
                    elif diff <= bricks:
                        bricks -= diff
                    else:
                        return i-1
                    
        return len(heights) -1