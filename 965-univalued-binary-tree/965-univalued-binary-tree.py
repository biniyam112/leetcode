# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,value):
            if not node:
                return True
            if node.val != value:
                return False
            return dfs(node.left,value) and dfs(node.right,value)
        return dfs(root,root.val)