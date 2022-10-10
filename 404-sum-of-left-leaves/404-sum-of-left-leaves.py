# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def recursion(node,left):
            if not node.left and not node.right:
                if left:
                    self.leftsum += node.val
                return
            if node.left:
                recursion(node.left,True)
            if node.right:
                recursion(node.right,False)
        self.leftsum = 0
        recursion(root,False)
        return self.leftsum
            
        