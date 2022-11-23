class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # column traversal
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[j][i] in visited:
                    return False
                if board[j][i] != '.':
                    visited.add(board[j][i])
        # row traversal
        for row in board:
            visited = set()
            for cell in row:
                if cell in visited:
                    return False
                if cell != '.':
                    visited.add(cell)
        # box traversal
        for t in range(3): 
            for i in range(3):
                visited = set()
                for j in range(3):
                    for k in range(3):
                        if board[(3*i)+j][(3*t)+k] in visited:
                            return False
                        if board[(3*i)+j][(3*t)+k] != '.':
                            visited.add(board[(3*i)+j][(3*t)+k])
        # for i in range(3):
        #     visited = set()
        #     for j in range(3):
        #         for k in range(3):
        #             if board[j][(3*i)+k] in visited:
        #                 return False
        #             if board[j][(3*i)+k] != '.':
        #                 visited.add(board[j][(3*i)+k])
        return True
    
    # time = n2 where n = len(board)
    # space = 1 or (n * (0.5)) lol
        