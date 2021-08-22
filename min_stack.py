class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.body = []
        self.asc = [] 
        

    def push(self, val: int) -> None:
        self.body.append(val)
        
        ptr = 0
        for i in range(len(self.asc)):
            if(self.asc[i] >= val):
                ptr = i
                break
            else:
                ptr += 1
        self.asc.insert(ptr, val)
        

    def pop(self) -> None:
        item = self.body.pop()
        self.asc.remove(item)

    def top(self) -> int:
        return self.body[-1]

    def getMin(self) -> int:
        return self.asc[0]


