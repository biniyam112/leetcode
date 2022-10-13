# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        covered = {None}
        self.counter = 0
        def dfs(node,par):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if (par is None and node not in covered or node.left not in covered or node.right not in covered):
                    self.counter += 1
                    covered.update({node, par, node.left, node.right})
        dfs(root,None)
        return self.counter