# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def recursion(node,sum_):
            if not node.right and not node.left:
                if sum_+node.val == targetSum:
                    return True
                return False
            left,right = False,False
            if node.left:
                left = recursion(node.left,sum_+node.val)
            if node.right:
                right = recursion(node.right,sum_+node.val)
            return left or right
        return recursion(root,0)