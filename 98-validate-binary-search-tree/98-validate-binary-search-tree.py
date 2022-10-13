# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder with constant space
        self.last = float('-inf')
        def recursion(node):
            if not node:
                return True
            left = recursion(node.left)
            if node.val <= self.last:
                return False
            self.last = node.val
            right = recursion(node.right)
            return left and right 
        return recursion(root)
        
        
        
        # by inorder traversal
        # nums = []
        # def inorder(node):
        #     if not node:
        #         return
        #     inorder(node.left)
        #     nums.append(node.val)
        #     inorder(node.right)
        # inorder(root)
        # for i in range(len(nums)-1):
        #     if nums[i] >= nums[i+1]:
        #         return False
        # return True
        
        # time_comp = n
        # space_comp = n