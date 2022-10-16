class Solution:
    def minDifficulty(self, jobDiff: List[int], days: int) -> int:
        n = len(jobDiff)
    
        @cache
        # dp(i, k): min difficulty when you start working on i-th job at day `k`
        def dp(i, k):
            # reach the last day
            # we put all the remaining jobs on this day
            # so we return the one with max difficulty
            if k == days: return max(jobDiff[i:])
            # init min difficulty with inf 
            res = float('inf')
            # cur is the max difficulty we've seen so far on day `k`
            # init current max with 0
            cur = 0
            # for jobDifficulty like 6 5 4 3 2 1, 
            # we can have following ways to distribute them into two days
            # 6 | 5 4 3 2 1
            # 6 5 | 4 3 2 1 
            # 6 5 4 | 3 2 1
            # 6 5 4 3 | 2 1
            # 6 5 4 3 2 | 1
            # notice that each day we must have at least one task
            # given the starting index `i`, 
            # we can only at most choose the jobs till the position `n - d + k - 1`
            for j in range(i, n - days + k):
                cur = max(cur, jobDiff[j])
                # if j-th job is the last job on day `k`, 
                # the max difficulty for day `k` is `cur`
                # and we need to start (j + 1)-th job on the next day
                # the result would be `cur + dp(j + 1, k + 1)`
                # then we take the min
                res = min(res, cur + dp(j + 1, k + 1))
            return res
        # n < d : you will have free days. hence you cannot find a schedule for the given jobs
        # e.g. Example 2
        # otherwise, we start working on 0-th job at day 1
        return -1 if n < days else dp(0, 1)
        def dp(index,curDay,days_max):
            if (index,curDay) in visited:
                return visited[(index,curDay)]
            if index == len(jobDiff):
                if curDay == days-1:
                    return sum(days_max)
                return float('inf')
            if curDay == days-1:
                days_max[curDay] = max(days_max[curDay],jobDiff[index])
                return dp(index+1,curDay,days_max)
            if days_max[curDay] == float('-inf'):
                days_max[curDay] = jobDiff[index]
                return dp(index+1,curDay,days_max)
            # add to cur day
            cur_day_days_max = days_max.copy()
            cur_day_days_max[curDay] = max(cur_day_days_max[curDay],jobDiff[index])
            to_cur_day = dp(index+1,curDay,cur_day_days_max)
            # add to next day
            next_day_days_max = days_max
            next_day_days_max[curDay+1] = jobDiff[index]
            to_next_day = dp(index+1,curDay+1,days_max)
            visited[(index,curDay)] = min(to_cur_day,to_next_day)
            return min(to_cur_day,to_next_day)
        
        visited = {}
        days_max = [float('-inf')] * days
        return -1 if days > len(jobDiff) else dp(0,0,days_max)
                    
                    
            