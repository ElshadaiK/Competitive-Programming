class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        row = len(matrix)
        col = len(matrix[0])
        self.prefix = []
        for i in range(row):
            temp = [matrix[i][0]]
            for j in range(1, col):
                temp.append(matrix[i][j]+temp[-1])
            self.prefix.append(temp)
                
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            if(col1 > 0):
                prev = self.prefix[i][col1-1]
            else:
                prev = 0
            ans += self.prefix[i][col2] - prev
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)