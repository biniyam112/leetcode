class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        counter = [0] * n

        for i in range(n):
            count = 0
            for j in range(n-1,-1,-1):
                if grid[i][j] == 0:
                    count += 1
                else:
                    break
            counter[i] = count
        
        def find_row(i,zeros):
            if counter[i] >= zeros:
                return 0
            steps = float('inf')
            if i+1 < n:
                steps = min(steps, 1+find_row(i+1,zeros))
            return steps
        
        def swap(top,bottom):
            for i in range(bottom,top,-1):
                counter[i],counter[i-1] = counter[i-1],counter[i]

        steps = 0
        for i in range(n):
            min_steps = find_row(i,n-i-1)
            if min_steps > n: return -1
            steps += min_steps
            swap(i,i+min_steps)
        return steps