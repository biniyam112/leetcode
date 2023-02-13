class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[-1][-1] == 1 or grid[0][0] == 1:
            return -1
        queue = deque()
        n = len(grid)
        queue.append((0,0))
        directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
        inbound = lambda row,col :  0 <= row < n and 0 <= col < n
        output = 1
        visited = {(0,0):1}
        while queue:
            cell = queue.popleft()
            if cell[0] == cell[1] == n-1:
                return visited[(n-1,n-1)]
            for path in directions:
                new_row,new_col = cell[0]+path[0],cell[1]+path[1]
                if inbound(new_row,new_col) and (new_row,new_col) not in visited and grid[new_row][new_col] == 0:
                    visited[(new_row,new_col)] = visited[cell]+1
                    queue.append((new_row,new_col))
        return -1
            
        
        
        