class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        cursum  = 0
        
        for i,val in enumerate(nums):
            cursum += val
            if cursum > ans:
                ans = cursum
            if cursum < 0:
                cursum = 0
        return ans