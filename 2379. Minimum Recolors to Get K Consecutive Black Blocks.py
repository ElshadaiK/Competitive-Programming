class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n, minOps, flips, count, i = len(blocks), float('inf'), 0, 0, 0
        for j in range (n):
            if blocks[j] == 'W':
                flips += 1
                count += 1
            elif blocks[j] == 'B':
                count += 1
            if count == k:
                minOps = min(minOps, flips)
                if blocks[i] == 'W':
                    flips -= 1
                    count -= 1
                else: count -= 1
                i += 1
        return minOps
