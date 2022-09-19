# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def dfs(node,path):
            if not node.right and not node.left:
                paths.append(path+str(node.val))
                return
            if node.right:
                dfs(node.right,path+str(node.val)+'->')
            if node.left:
                dfs(node.left,path+str(node.val)+'->')
        dfs(root,'')
        return paths