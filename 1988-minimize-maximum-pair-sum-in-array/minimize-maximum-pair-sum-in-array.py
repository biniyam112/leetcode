class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        start,end = 0, len(nums)-1

        ans = 0
        while start < end:
            ans = max(ans,nums[end]+nums[start])
            start += 1
            end -= 1
        return ans

        