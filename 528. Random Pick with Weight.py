class Solution:

    def __init__(self, w: List[int]):
        self.array = []
        self.SUM = sum(w)
        self.LENGTH = len(w)
        self.PERCENT = 100
        
        for idx, weight in enumerate(w):
            frequency = math.ceil(weight * self.LENGTH * self.PERCENT / self.SUM)
            self.array += [idx] * frequency
        

    def pickIndex(self) -> int:
        return self.array[random.randrange(len(self.array))]
        