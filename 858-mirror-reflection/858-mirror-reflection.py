class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if(p == q):
            return 1
        elif(p/2 == q):
            return 2
        else:
            gcf = self.gcf(p,q)
            wall = q//gcf%2 - p//gcf%2
            return (wall+1)
        
    def gcf(self, a, b):
        i = min(a,b)
        while(i >= 1):
            if(a%i == 0 and b%i == 0):
                return i
            i -= 1