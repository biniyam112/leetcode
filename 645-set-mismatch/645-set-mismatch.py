class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        output = []
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                output.append(nums[i])
                break
        nums = set(nums)
        for i in range(1,len(nums)+2):
            if i not in nums:
                output.append(i)
        return output