class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #2    7    11    15   target = 14
    #      ij
    # add every element in set
    # iterate on each item and check if target - num is in the set
        # i = 0
        # j = len(nums)-1
        # nums.sort()
        # while i <= j:
        #     sum_ = nums[i]+nums[j]
        #     if sum_ == target:
        #         return [i,j]
        #     elif sum_ > target:
        #         j -= 1
        #     else:
        #         i += 1
        items = defaultdict(int)
        for i,num in enumerate(nums):
            items[num] = i
        for i,num in enumerate(nums):
            if target - num in items and i != items[target-num]:
                return [items[target-num],i]