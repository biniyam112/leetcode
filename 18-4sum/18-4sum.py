class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
	
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            
            # If we have run out of numbers to add, return res.
            if not nums:
                return res
            
            # There are k remaining values to add to the sum. The 
            # average of these values is at least target // k.
            average_value = target // k
            
            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest 
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            
            if k == 2:
                return twoSum(nums, target)
    
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
    
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            s = set()
    
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])
    
            return res

        nums.sort()
        return kSum(nums, target, 4)






class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def diffExist(indices,indexSet):
            if len(indexSet) > 3 : return True
            for index in indexSet:
                if index not in indices:
                    return True
            return False
            
        valat = defaultdict(set)
        for i,val in enumerate(nums):
            valat[val].add(i)
         
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    cursum = nums[i]+nums[j]+nums[k]
                    rem = target - cursum
                    if diffExist([i,j,k],valat[rem]):
                        idx, *_ = valat[rem]
                        fsum = tuple(sorted([nums[i],nums[j],nums[k],nums[idx]]))
                        ans.add(fsum)
        return ans