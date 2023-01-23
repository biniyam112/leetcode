class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        places = defaultdict(list)
        for i,val in enumerate(nums):
            places[val].append(i)
            
        @cache
        def dp(diff,index):
            res = 0
            for place in places[nums[index]+diff]:
                if place > index:
                    res = max(res,1+dp(diff,place))
            return res
            
            
        ans = 2
        for i in range(n):
            for j in range(i+1,n):
                diff = nums[j]-nums[i]
                ans = max(ans,dp(diff,i)+1)
        return  ans
            
        
        
        
        