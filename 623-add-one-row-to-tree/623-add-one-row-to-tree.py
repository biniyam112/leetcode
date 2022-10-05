# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val,root)
        def recursion(curdepth,node):
            if not node:
                return
            if curdepth == depth-1:
                right = TreeNode(val,None,node.right)
                left = TreeNode(val,node.left,None)
                node.right = right
                node.left = left
                return
            else:
                recursion(curdepth+1,node.right)
                recursion(curdepth+1,node.left)
        recursion(1,root)                        
        return root