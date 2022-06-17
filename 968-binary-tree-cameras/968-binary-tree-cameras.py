# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if(not root): return 0
            val = dfs(root.left) + dfs(root.right)
            if(val == 0): return 3
            if(val < 3): return 0
            self.res += 1
            return 1
        return self.res + 1 if dfs(root) > 2 else self.res