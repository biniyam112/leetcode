class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ans = max(ans,nums[j]-nums[i])
        if ans == 0:
            return -1
        return ans