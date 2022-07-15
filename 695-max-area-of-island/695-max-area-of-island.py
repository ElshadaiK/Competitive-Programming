class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.visited = [[0 for _ in range(self.width)] for _ in range(self.height)]
        max_area = 0
        
        for x in range(self.height):
            for y in range(self.width):
                max_area = max(max_area, self.traverse(x, y))
        
        return max_area
                
    

    def traverse(self, x, y):
        
        if x < 0 or y < 0 or x >= self.height or y >= self.width:
            return 0
        
        if self.grid[x][y] == 0:
            return 0
        
        elif self.visited[x][y] == 0:
            self.visited[x][y] = 1
            return 1 + sum([self.traverse(x + del_x, y + del_y) for (del_x, del_y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]])
        else:
            return 0
        