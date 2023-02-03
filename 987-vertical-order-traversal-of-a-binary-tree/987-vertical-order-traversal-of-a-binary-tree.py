# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        colIndexing = defaultdict(list)
        rowIndexing = defaultdict(int)
        def traversal(node,col= 0,row=0):
            if not node:
                return 
            colIndexing[col].append((row,node.val))
            rowIndexing[node.val] = row
            traversal(node.right,col+1,row+1)
            traversal(node.left,col-1,row+1)
            
        traversal(root)
        minCol = 0
        for k,_ in colIndexing.items():
            minCol = min(minCol,k)
            
        # print(colIndexing,rowIndexing)
        ans = [[] for _ in range(len(colIndexing))]
        for k,v in colIndexing.items():
            v.sort()
            col  = []
            for _,node in v:
                col.append(node)
            ans[k-minCol] = col
            
        return ans
        