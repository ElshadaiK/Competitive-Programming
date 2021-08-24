class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        collect = {}
        results = []
        center = [rCenter, cCenter]
        for i in range(rows):
            for j in range(cols):
                value = [i, j]
                dist = self.distance(center, value)

                if(collect.get(dist)):
                    collect[dist].append(value)
                else:
                    collect[dist] = [value]

        for i in sorted(collect.keys()):
            for j in collect[i]:
                results.append(j)
        
        return results
    def distance(self, center, point):
        x =  abs(center[0] - point[0])
        y = abs(center[1] - point[1])
        return x+y