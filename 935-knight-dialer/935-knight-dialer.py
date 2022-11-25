class Solution:
    def knightDialer(self, n: int) -> int:
        
        moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,-2],[-1,-2],[1,2],[-1,2]]
        valid = lambda row,col : 0 <= row < len(board) and 0 <= col <len(board[0]) and board[row][col] != None
        

        board = [[[] for _ in range(3)] for _ in range(3)]
        board.append([None,[],None])
        
        ans = 0
        for i in range(4):
            for j in range(3):
                if board[i][j] != None:
                    for x,y in moves:
                        new_row,new_col = i+x,j+y
                        if valid(new_row,new_col):
                            board[i][j].append((new_row,new_col))
        
        def dfs(row,col,steps):
            if steps == n:
                return 1
            res = 0
            if (row,col,steps) in visited:
                return visited[(row,col,steps)]
            for cell in board[row][col]:
                res += dfs(cell[0],cell[1],steps+1)
            visited[(row,col,steps)] = res
            return res
        
            
        ans = 0
        visited = {}
        for i in range(4):
            for j in range(3):
                if board[i][j] != None:
                    ans += dfs(i,j,1)
        
        
        return ans % (10**9+7)
            
            
            
        