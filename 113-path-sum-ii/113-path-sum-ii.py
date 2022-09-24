# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def recursion(node,pathsum,path):
            if not node.right and not node.left:
                if pathsum == targetSum:
                    ans.append(path)
                return
            right = path.copy()
            left = path.copy()
            if node.right:
                right.append(node.right.val)
                recursion(node.right,pathsum+node.right.val,right)
            if node.left:
                left.append(node.left.val)
                recursion(node.left,pathsum+node.left.val,left)
                
        if not root:
            return []
        ans = []
        recursion(root,root.val,[root.val])
        return ans
            
                
        