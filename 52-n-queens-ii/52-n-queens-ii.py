class Solution:
    result = 0
    def totalNQueens(self, n: int) -> int:

        colSet = set()
        posDiagSet = set()
        negDiagSet = set()

        def backtrackingDFS(row):
            if row == n:
                self.result += 1
                return

            for col in range(0,n):
                if col not in colSet and (row-col) not in posDiagSet and (row+col) not in negDiagSet:
                    colSet.add(col)
                    posDiagSet.add(row-col)
                    negDiagSet.add(row+col)
                    backtrackingDFS(row+1)
                    colSet.remove(col)
                    posDiagSet.remove(row-col)
                    negDiagSet.remove(row+col)

        backtrackingDFS(0)

        return self.result