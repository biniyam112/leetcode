class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        inbound = lambda row,col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        m,n = len(grid),len(grid[0])
        
        coordinate = defaultdict(list)
        for i in range(m):
            for j in range(n):
                coordinate[grid[i][j]] = [i,j]
        # print(coordinate)
        
        def dfs(row,col):
            if row == len(grid)-1:
                return grid[row][col]
            if grid[row][col] in visited:
                return visited[grid[row][col]]
            minCost = float('inf')
            for j in range(n):
                minCost = min(minCost,grid[row][col] + moveCost[grid[row][col]][j] + dfs(row+1,j))
            visited[grid[row][col]] = minCost
            return minCost
        
        ans = float('inf')
        visited = {}
        for j in range(n):
            ans = min(ans,dfs(0,j))
        return ans