class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        j=len(matrix[0])-1
        while(i<len(matrix) and j>=0):
            if target<matrix[i][j]:
                j-=1
            elif target>matrix[i][j]:
                i+=1
            else:
                return True
        return False