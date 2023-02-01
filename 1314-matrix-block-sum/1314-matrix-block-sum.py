class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        presum = []
        
        for i in range(m):
            row = [mat[i][0]]
            for j in range(1,n):
                row.append(row[-1]+mat[i][j])
            presum.append(row)
        
        # print(presum)
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s_row,s_col = [max(0,i-k),max(0,j-k)]
                e_row,e_col = [min(m-1,i+k),min(n-1,j+k)]
                for r in range(s_row,e_row+1):
                    res[i][j] += presum[r][e_col]
                    if s_col > 0:
                        res[i][j] -= presum[r][s_col-1]
        return res
                
        