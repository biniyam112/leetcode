class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = [0] * len(grid[0])
        inbound = lambda col : 0 <= col < len(grid[0])
        def simulator(col):
            for row in range(len(grid)):
                prev = col
                col += grid[row][col]
                if not inbound(col) or grid[row][prev] != grid[row][col]:
                    return -1
            return col
        for col in range(len(grid[0])):
            ans[col] = simulator(col)
        return ans
            