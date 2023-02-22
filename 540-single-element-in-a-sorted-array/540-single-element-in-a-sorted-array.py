class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        while i < j:
            mid = i + (j-i)//2
            if nums[mid-1] != nums[mid] != nums[mid+1]:
                return nums[mid]
            from_start = mid-i
            if from_start % 2 and nums[mid-1] == nums[mid]:
                i = mid+1
            elif from_start % 2 == 0 and nums[mid-1] != nums[mid]:
                i = mid+2
            elif from_start % 2 == 0 and nums[mid-1] == nums[mid]:
                j = mid-2
            elif from_start % 2 == 1 and nums[mid-1] != nums[mid]:
                j = mid-1
        return nums[i]
                
                