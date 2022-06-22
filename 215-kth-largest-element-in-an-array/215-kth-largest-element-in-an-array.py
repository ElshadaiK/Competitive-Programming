class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        klargest = [float('-Inf')]*k
        heapq.heapify(klargest)
        for num in nums:
            heapq.heappushpop(klargest, num)
        return klargest[0]