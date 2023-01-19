
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        
                
        
        
        maxsum = float('-inf')
        minsum = float('inf')
        curmax = 0
        curmin = 0
        for i,val in enumerate(nums):
            curmax += val
            curmin += val
            maxsum = max(curmax,maxsum)
            minsum = min(curmin,minsum)
            curmax = max(curmax,0)
            curmin = min(curmin,0)
                
        total = sum(nums)
        if total == minsum: return maxsum
        return max(maxsum,total-minsum)
            
                