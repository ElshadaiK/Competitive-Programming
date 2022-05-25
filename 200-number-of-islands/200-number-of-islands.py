class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        def dfs(x,y):
            for i, j in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_x, new_y = x+i, y+j
                if(new_x >= 0 and new_x < row and new_y >= 0 and new_y < col and ((new_x, new_y) not in visited)
                  and grid[new_x][new_y] == "1"):
                    visited.add((new_x, new_y))
                    dfs(new_x, new_y)
                    
        island = 0
        for i in range(row):
            for j in range(col):
                if((i,j) not in visited and grid[i][j] == "1"):
                    visited.add((i,j))
                    island += 1
                    dfs(i,j)
        return island
                