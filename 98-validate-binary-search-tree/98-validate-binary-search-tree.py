# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min, max):

            return (
                (min < node.val < max) and 
                (not node.left or dfs(node.left, min, node.val)) and 
                (not node.right or dfs(node.right, node.val, max))
            )

        return dfs(root, -inf, inf)