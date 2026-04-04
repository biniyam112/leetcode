class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        #can be done with djkistra
        m,n = len(rowCosts), len(colCosts)
        inbound = lambda row,col : 0 <= row < m and 0 <= col < n

        def recursion(row,col):
            if [row,col] == homePos:
                return 0
            home_row,home_col = homePos
            if row < home_row:
                return rowCosts[row+1] + recursion(row+1,col)
            elif row > home_row:
                return rowCosts[row-1] + recursion(row-1,col)

            if col < home_col:
                return colCosts[col+1] + recursion(row,col+1)
            elif col > home_col:
                return colCosts[col-1] + recursion(row,col-1)
        
        return recursion(*startPos)