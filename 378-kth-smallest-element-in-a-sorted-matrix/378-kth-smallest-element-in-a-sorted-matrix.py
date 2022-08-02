class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxheap = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row+1) * (col+1) > k:
                    break
                num = matrix[row][col]
                if len(maxheap) < k:
                    heapq.heappush(maxheap, -num)
                elif num < -maxheap[0]:
                    heapq.heappushpop(maxheap, -num)
        return -maxheap[0]