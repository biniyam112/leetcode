class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        starts = []
        for i in range(len(grid)):
            for j in range(len(grid)):                
                starts.append((i,j))
        for start in starts:
            row,col = start[0],start[1]
            equal = True
            for i in range(len(grid)):
                if grid[row][i] != grid[i][col]:
                    equal = False
                    break
            if equal: 
                count += 1 
        return count