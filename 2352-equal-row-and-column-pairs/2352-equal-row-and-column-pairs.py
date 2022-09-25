class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid)):                
                equal = True
                for k in range(len(grid)):
                    if grid[i][k] != grid[k][j]:
                        equal = False
                        break
                if equal: count += 1 
        return count