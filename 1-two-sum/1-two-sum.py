class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #2    7    11    15   target = 14
    #      ij
    # add every element in set
    # iterate on each item and check if target - num is in the set
        i = 0
        j = len(nums)-1
        for k,num in enumerate(nums):
            nums[k] = (num,k)
        nums.sort()
        while i < j:
            sum_ = nums[i][0] + nums[j][0]
            if sum_ == target:
                return [nums[i][1],nums[j][1]]
            elif sum_ > target:
                j -= 1
            else:
                i += 1