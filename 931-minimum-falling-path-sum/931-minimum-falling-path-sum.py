class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        inbound = lambda row,col : 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        dirs = [[1,-1],[1,0],[1,1]]
        visited = {}
        
        def dfs(row,col):
            if row == len(matrix)-1:
                return matrix[row][col]
            if (row,col) in visited:
                return visited[(row,col)]
            min_ = float('inf')
            for dir_ in dirs:
                new_row,new_col = row + dir_[0],col + dir_[1]
                if inbound(new_row,new_col):
                    cur = dfs(new_row,new_col)
                    min_ = min(min_,cur)
            # print(matrix[row][col],min_)
            visited[(row,col)] = matrix[row][col] + min_
            return matrix[row][col] + min_
        
        
        min_ = float('inf')
        for i in range(len(matrix[0])):
            min_ = min(min_,dfs(0,i))
        return min_