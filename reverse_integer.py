class Solution:
    def reverse(self, x: int) -> int:
        result = ""
        negation = False
        if(x<0):
            negation = True
            x = x*(-1)
        if(len(str(x)) == 1):
            result += str(x)
            return result
        while(x>0):
            result += str(x%10)
            x = x//(10)
        x = int(result)
        if((x >= 2**31 and result == "") or (x > 2**31 and result != "")):
            return 0
        if(negation):
            x *= -1
        return x
                          