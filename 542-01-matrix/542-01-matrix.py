class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        inbound = lambda row,col : 0 <= row < len(mat) and 0 <= col < len(mat[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        
        def bfs(queue):            
            while queue:
                row,col,steps = queue.popleft()
                mat[row][col] = steps
                for x,y in dirs:
                    new_row,new_col = row+x,col+y
                    if inbound(new_row,new_col) and (new_row,new_col) not in visited:
                        visited.add((new_row,new_col))
                        queue.append((new_row,new_col,steps+1))
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    mat[i][j] = float('inf')
        queue = deque()
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
                    visited.add((i,j))
        bfs(queue)
                    
        
        return mat                                                      
            