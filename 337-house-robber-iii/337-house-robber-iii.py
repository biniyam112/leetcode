# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def recursion(node,robbed):
            right = 0
            left = 0
            if node.right:
                if not robbed:
                    right = recursion(node.right,True)
                right = max(right,recursion(node.right,False))
            if node.left:
                if not robbed:
                    left = recursion(node.left,True)
                left = max(left,recursion(node.left,False))
            if robbed:
                return right+left+node.val
            return right+left
        return max(recursion(root,False),recursion(root,True))
        