class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort() # nlogn
        heap = [] 
        heapq.heappush(heap, intervals[0][1])
        meetingRooms = 1
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if(interval[0] >= heap[0]):
                heapq.heappop(heap)
            else:
                meetingRooms += 1
            heapq.heappush(heap, interval[1])
        return meetingRooms
                
        
