# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:   
        def recursion(node,pathsum):
            if not node.left and not node.right:
                return pathsum+node.val
            left = float('-inf')
            right = float('-inf')
            if node.left:
                left = recursion(node.left,pathsum+node.val)
            if node.right:
                right = recursion(node.right,pathsum+node.val)
            # print(node.val,left,right)
            if left < limit:
                node.left = None
            if right < limit:
                node.right = None
            pathsum = max(left,right)
            return pathsum
        
        pathsum = recursion(root,0)
        if pathsum < limit:
            return None
        return root

