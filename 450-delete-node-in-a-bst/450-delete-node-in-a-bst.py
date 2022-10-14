# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        def dfs(node,par=TreeNode(val=float('inf')),isleft=True):
            if node.val == key:
                # no right and left child
                if not node.right and not node.left:
                    if isleft:
                        par.left = None
                    else:
                        par.right = None
                # has right child only
                elif not node.left:
                    if isleft:
                        par.left = node.right
                    else:
                        par.right = node.right
                # has left child only
                elif not node.right:
                    if isleft:
                        par.left = node.left
                    else:
                        par.right = node.left
                # have right and left child
                else:
                    left = node.left
                    right = node.right
                    if isleft:
                        temp = right
                        while temp.left:
                            temp = temp.left
                        temp.left = left
                        par.left = right
                    else:
                        temp = left
                        while temp.right:
                            temp = temp.right
                        temp.right = right
                        par.right = left
                return
            if node.left:
                dfs(node.left,node,True)
            if node.right:
                dfs(node.right,node,False)

        root_val = root.val
        if root_val == key:
            root = TreeNode(float('inf'),root)
            dfs(root)
            return root.left
        dfs(root)
        return root