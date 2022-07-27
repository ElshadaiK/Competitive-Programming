# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None or (root.left is None and root.right is None):
            return root
        
        left_end = None
        if root.left:
            left_end = self.flatten(root.left)
            
        right_end = None
        if root.right:
            right_end = self.flatten(root.right)
            
        if root.left and root.right:
            root.right, left_end.right, root.left = root.left, root.right, None
            return right_end
        elif root.left:
            root.right, root.left = root.left, None
            return left_end
        else:
            return right_end