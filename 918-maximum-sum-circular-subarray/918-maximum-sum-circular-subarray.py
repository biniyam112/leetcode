
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        
                
        
        
        maxsum = float('-inf')
        cursum = 0
        for i,val in enumerate(nums):
            cursum += val
            if cursum > maxsum:
                maxsum = cursum
            if cursum < 0:
                cursum = 0
                
        minsum = float('inf')
        cursum = 0
        for i,val in enumerate(nums):
            cursum += val
            if cursum < minsum:
                minsum = cursum
            if cursum > 0:
                cursum = 0
        
        total = sum(nums)
        # print(total,minsum)
        if total == minsum:
            return maxsum
        return max(maxsum,total-minsum)
            
                