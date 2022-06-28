class Solution:
    def minDeletions(self, s: str) -> int:
        store = {}
        for i in range(len(s)):
            item = s[i]
            if(item not in store):
                store[item] = 0
            store[item] += 1
        heap = []
        deleted = 0
        for key in store:
            val = store[key]
            heapq.heappush(heap, (-val, key))
        while(len(heap) > 1):
            count, item = heapq.heappop(heap)
            count *= -1
            if(count == 0):
                break
            while(True):
                i, j = heapq.heappop(heap)
                if(-i < count):
                    heapq.heappush(heap, (i, j))
                    break
                elif(-i == count):
                    deleted += 1
                    heapq.heappush(heap, (i+1, j))
        return deleted