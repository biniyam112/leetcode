class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        zipped = sorted(zip(ages,scores),key = lambda pair : (-pair[0],-pair[1]))
        n = len(zipped)

        ans = 0
        dp = [0] * n
        for i in range(n):
            _,score = zipped[i]
            for j in range(i,-1,-1):
                _,prev_score = zipped[j]
                if prev_score >=  score:
                    dp[i] = max(dp[i],dp[j]+score)
            ans = max(ans, dp[i])
        return ans
            
            
        
        
        
                
        for i in range(n):
            ages[i],scores[i] = zipped[i][0], zipped[i][1]
            
        visited = defaultdict(int)
        def dp(index,minscore = float('inf')):
            if index == n:
                return 0
            if scores[index] > minscore:
                return dp(index+1,minscore)
            if (index,minscore) in visited:
                return visited[(index,minscore)]
            curmin = min(minscore,scores[index])
            res = max(scores[index]+dp(index+1,curmin),dp(index+1,minscore))
            visited[(index,minscore)] = res
            return res
        return dp(0)
            