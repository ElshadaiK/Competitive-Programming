class Solution:
    def addQueen(self,result,output,n):
        temp = []
        for i in result:
            queen = '.'*i+'Q'+'.'*(n-i-1)
            temp.append(queen)
        output.append(temp)
    
    def backtracking(self,result,col,posD,negD,n,output):
        if len(result)==n:
            self.addQueen(result,output,n)
            return
        row = len(col)-1
        for i in range(n):
            if i in col or (row-i) in negD or (row+i) in posD:
                continue
            result.append(i)
            col.add(i)
            posD.add(row+i)
            negD.add(row-i)
            self.backtracking(result,col,posD,negD,n,output)
            col.remove(i)
            posD.remove(row+i)
            negD.remove(row-i)
            result.pop(-1)
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        self.backtracking([],set(),set(),set(),n,output)
        return output