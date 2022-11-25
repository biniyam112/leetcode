class Solution:
    def knightDialer(self, n: int) -> int:
        
        
        keys = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],[1, 7, 0], [2, 6], [1, 3], [2, 4]]
        
        ans = 0
        def dfs(key,steps):
            if steps == n:
                return 1
            res = 0
            if (key,steps) in visited:
                return visited[(key,steps)]
            for next_key in keys[key]:
                res += dfs(next_key,steps+1)
            visited[(key,steps)] = res
            return res
        
        
        ans = 0
        visited = {}
        for i in range(len(keys)):
            ans += dfs(i,1)
        return ans % (10**9+7)
            
            
            
        