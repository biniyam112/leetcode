
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        
                
        rightmax = [float('-inf')] * n
        suffixsum = rightmax[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            suffixsum += nums[i]
            rightmax[i] = max(suffixsum,rightmax[i+1])
        
        
        maxsum = float('-inf')
        specialsum = float('-inf')
        cursum = 0
        presum = 0
        for i,val in enumerate(nums):
            cursum += val
            presum += nums[i]
            if cursum > maxsum:
                maxsum = cursum
            if cursum < 0:
                cursum = 0
            if i+1 < n:
                specialsum = max(specialsum,presum+rightmax[i+1])
                
        return max(maxsum,specialsum)
            
                