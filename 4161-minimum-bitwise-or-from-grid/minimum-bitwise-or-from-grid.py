class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        best = float('inf')
        m,n = len(grid),len(grid[0])
        grido = [None for i in range(m)]

        for i in range(m):
            grid[i].sort()
            grido[i] = set(grid[i])

        @cache
        def recursion(i,j,val):
            nonlocal best
            if val >= best:
                return
            if i == m:
                best = min(best,val)
                return
            if val in grido[i]:
                recursion(i+1,0,val)
            else:
                for k in range(j,n):
                    val_new = val | grid[i][k]
                    recursion(i+1,0,val_new)

        recursion(0,0,0)
        return best
                
                