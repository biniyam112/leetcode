class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        dirs = [(1,0),(0,1),(1,1)]
        inbound = lambda row,col : 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        
        
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(i>0 and j>0 and matrix[i][j]=='1'): matrix[i][j] = min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j]) + 1
                matrix[i][j] = int(matrix[i][j])
                res = max(res,matrix[i][j])
        return res*res
            
        
        def bfs(row,col):
            layer = [(row,col)]
            size = 1
            while True:
                newLayer = set()
                while layer:
                    row,col = layer.pop()
                    for x,y in dirs:
                        new_row,new_col = row+y,col+x
                        if not inbound(new_row,new_col) or matrix[new_row][new_col] == "0" or (new_row,new_col) in visited:
                            return size
                        newLayer.add((new_row,new_col))
                visited.update(newLayer)
                layer = newLayer
                size += 1
                
        maxSquare = 0
        visited  = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1" and  len(matrix)-i > maxSquare and len(matrix[0])-j > maxSquare:
                    maxSquare = max(maxSquare,bfs(i,j))
        return maxSquare** 2
        
        