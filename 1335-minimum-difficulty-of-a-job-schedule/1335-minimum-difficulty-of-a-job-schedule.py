class Solution:
    def minDifficulty(self, jobDiff: List[int], days: int) -> int:    
        n = len(jobDiff)
        @cache
        def dp(index,curday):
            if curday == days:
                return max(jobDiff[index:])
            res = float('inf')
            cur = 0
            for i in range(index,n-days+curday):
                cur = max(cur,jobDiff[i])
                res = min(res,cur+dp(i+1,curday+1))
            return res
        return -1 if days > n else dp(0,1)
                    
                    
            