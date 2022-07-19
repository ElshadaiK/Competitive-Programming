class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0: return []
        res = [[1]]
        for i in range(1, numRows):
            temp = []
            temp.append(1)
            j = 0
            while(len(temp) < len(res[i-1])):
                val = res[i-1][j] + res[i-1][j+1]
                temp.append(val)
                j += 1
            temp.append(1)
            res.append(temp)
        return res
            