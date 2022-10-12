class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i,j,k = 0,1,2
        while k < len(nums):
            if nums[j]+nums[k] > nums[i]:
                return sum(nums[i:k+1])
            i,j,k = j,k,k+1
        return 0
            