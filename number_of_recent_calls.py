class RecentCounter:
    
    def __init__(self):
        self.requests = []
        self.range = []
        self.counter = 0
        self.ptr = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.counter += 1
        self.range = [t-3000, t]
    
        for i in range(self.ptr, len(self.requests)):
            if(self.requests[i] < self.range[0]):
                self.counter -= 1
            else:
                self.ptr = i
                break
        return self.counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)