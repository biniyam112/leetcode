# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def recursion(node):
            if not node.right and val > node.val:
                node.right = TreeNode(val)
                return
            if not node.left and val < node.val:
                node.left = TreeNode(val)
                return
            if val  > node.val and node.right:
                recursion(node.right)
            if  val < node.val  and node.left:
                recursion(node.left)
        recursion(root)
        return root
                        