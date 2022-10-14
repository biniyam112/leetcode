# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.lastvisit,self.mindiff = float('-inf'),float('inf')
        def inorder(node):
            if node.left:
                inorder(node.left)
            self.mindiff = min(self.mindiff,node.val-self.lastvisit)
            self.lastvisit = node.val
            if node.right:
                inorder(node.right)
            
        inorder(root)
        return self.mindiff
    
    
    
        # def dfs(node,par=float('inf'),leftside=True):
        #     if node.left:
        #         if not leftside and node.val != root.val:
        #             # print('left',node.left.val,node.val,par)
        #             self.mindiff = min(self.mindiff,node.left.val-par)
        #             par = node.val
        #         self.mindiff = min(self.mindiff,node.val-node.left.val)
        #         dfs(node.left,par,True)
        #     if node.right:
        #         if leftside and node.val != root.val:
        #             # print('right',node.right.val,node.val,par)
        #             self.mindiff = min(self.mindiff,par-node.right.val)
        #             par = node.val
        #         self.mindiff = min(self.mindiff,node.right.val-node.val)
        #         dfs(node.right,par,False)
            
        # self.mindiff = float('inf')
        # dfs(root,root.val)
        # return self.mindiff
                
        