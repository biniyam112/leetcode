class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        inbound = lambda row,col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        dirs = [[1,0],[0,1]]

        def dfs(row,col):
            if row == len(grid)-1 and col == len(grid[0])-1:
                visited[(row,col)] = grid[row][col]
                return grid[row][col]
            cur_min = float('inf')
            for dir_ in dirs:
                new_row,new_col = row + dir_[0] , col + dir_[1]
                if inbound(new_row,new_col)  and (new_row,new_col) not in visited:
                    cur_min = min(cur_min , grid[row][col]+dfs(new_row,new_col))
                elif (new_row,new_col) in visited:
                    cur_min = min(cur_min,grid[row][col]+visited[(new_row,new_col)])
            visited[(row,col)] = cur_min
            return cur_min
            
            
        visited = {}
        dfs(0,0)
        return visited[(0,0)]
                    
            