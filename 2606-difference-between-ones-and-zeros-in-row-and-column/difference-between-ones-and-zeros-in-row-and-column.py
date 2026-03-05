class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid),len(grid[0])

        rows = [0] * m
        cols =[0] * n

        for i in range(m):
            for j in range(n):
                rows[i] += 1 if grid[i][j] else -1
                cols[j] += 1 if grid[i][j] else -1
        
        for i in range(m):
            for j in range(n):
                grid[i][j] = rows[i]+cols[j]
        return grid
