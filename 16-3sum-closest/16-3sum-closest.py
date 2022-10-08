class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 3 pointers soln
        i = 0
        j = len(nums)-1
        k = i+1
        mindiff  = float('inf')
        indices = ()
        nums.sort()
        while j > i+1:
            cursum = nums[i]+nums[j]+nums[k]
            if mindiff > abs(cursum-target):
                indices = (i,j,k)
                mindiff = abs(cursum-target)
            if cursum == target:
                return target
            if cursum > target and k == i+1:
                j -= 1
            elif cursum > target:
                if nums[i]+nums[j]+nums[k-1] < target:
                    i+=1
                k -= 1
            elif cursum < target and k == j-1:
                i += 1
            elif cursum < target:
                if nums[i]+nums[j]+nums[k+1] > target:
                    j-=1
                k += 1
        return nums[indices[0]]+nums[indices[1]]+nums[indices[2]]
        
            
            
        
        