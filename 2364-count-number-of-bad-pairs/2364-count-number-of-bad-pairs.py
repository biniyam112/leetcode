class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        def findgoods(num):
            return int((num+1) * num/2)
        bads = findgoods(len(nums)) 
        vals = defaultdict(int)
        for i in range(len(nums)):
            vals[nums[i]-i] += 1
        for k,v in vals.items():
            bads -= findgoods(v)
        return bads
            
            
        