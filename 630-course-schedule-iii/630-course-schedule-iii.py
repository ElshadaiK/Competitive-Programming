class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: (x[1], x[0]))
        heap = []
        time = 0
        for duration, lastday in courses:
            if(duration <= lastday):
                if(time+duration <= lastday):
                    time += duration
                    heapq.heappush(heap, -duration)
                elif(-heap[0] > duration):
                    time += heapq.heappop(heap) + duration
                    heapq.heappush(heap, -duration)
        return len(heap)