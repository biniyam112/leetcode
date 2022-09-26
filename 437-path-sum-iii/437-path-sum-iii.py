class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        global ans
        ans=0
        def solver(r):
            if not r:
                return 0
            iterator(r,0)
            solver(r.left)
            solver(r.right)
        def iterator(r,curr_sum):
            global ans
            if not r:
                return 0
            curr_sum+=r.val
            if curr_sum==targetSum:
                ans+=1
            iterator(r.left,curr_sum)
            iterator(r.right,curr_sum)
        solver(root)
        return ans
