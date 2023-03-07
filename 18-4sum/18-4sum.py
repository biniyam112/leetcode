class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()
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
                    if diffExist(set([i,j,k]),valat[rem]):
                        idx, *_ = valat[rem]
                        fsum = tuple(sorted([nums[i],nums[j],nums[k],nums[idx]]))
                        ans.add(fsum)
        return ans