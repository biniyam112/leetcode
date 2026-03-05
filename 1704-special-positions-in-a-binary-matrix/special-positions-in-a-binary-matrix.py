class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        m,n = len(mat), len(mat[0])

        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                rows[i] += mat[i][j]
                cols[j] += mat[i][j]
        
        # print(rows,cols)
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rows[i]+cols[j] == 2:
                    ans += 1
        return ans
            
        