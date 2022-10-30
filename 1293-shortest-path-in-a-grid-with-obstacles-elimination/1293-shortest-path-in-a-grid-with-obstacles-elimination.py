class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        inbound = lambda row,col : 0 <= row < m and 0 <= col < n 
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        queue = deque()
        queue.append((0,0,k,0))
        visited = set()
        
        while queue:
            row,col,k,steps = queue.popleft()
            # visited.add((row,col,k))
            if (row,col) == (m-1,n-1):
                return steps
            for x,y in dirs:
                nrow,ncol = row+y,col+x
                if inbound(nrow,ncol) and (nrow,ncol,k) not in visited:
                    if grid[nrow][ncol] == 0:
                        queue.append((nrow,ncol,k,steps+1))
                        visited.add((nrow,ncol,k))
                    elif grid[nrow][ncol] == 1 and k > 0:
                        queue.append((nrow,ncol,k-1,steps+1))
                        visited.add((nrow,ncol,k))
        return -1
        