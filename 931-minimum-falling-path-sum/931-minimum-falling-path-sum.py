class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp
        dp = [[float('inf') for _ in matrix[0]] for _ in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    dp[0][j] = matrix[0][j]
                else:
                    for k in (-1,0,1):
                        if j+k >= 0 and j+k < len(matrix[0]):
                            # print(dp[i][j],dp[i-1][j+k],matrix[i][j])
                            dp[i][j] = min(dp[i][j] , dp[i-1][j+k]+matrix[i][j])
        ans = float('inf')
        # print(dp)
        for val in dp[-1]:
            ans = min(ans,val)
        return ans
                