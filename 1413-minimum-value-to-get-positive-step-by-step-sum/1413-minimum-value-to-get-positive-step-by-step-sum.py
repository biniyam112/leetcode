class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pre = [0] * (len(nums)+1)
        val = 0
        for i in range(len(nums)):
            pre[i+1] = pre[i]+nums[i]
            if pre[i+1] <= 0:
                val += abs(pre[i+1])+1
                pre[i+1] += abs(pre[i+1])+1
        if val == 0:
            return 1
        return val
            
            
        