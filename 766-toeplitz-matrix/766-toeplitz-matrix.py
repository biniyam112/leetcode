class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m,n = len(matrix),len(matrix[0])
        inbound = lambda row,col: 0 <= row < m and 0 <= col < n
        for col in range(n):
            val = matrix[0][col]
            row = 0
            while inbound(row,col+row):
                if matrix[row][row+col] != val:
                    return False
                row += 1
        for row in range(m):
            val = matrix[row][0]
            col = 0
            while inbound(row+col,col):
                if matrix[row+col][col] != val:
                    return False
                col += 1
        return True
            
        