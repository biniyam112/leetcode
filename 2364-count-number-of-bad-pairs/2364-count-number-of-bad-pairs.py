class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        def findgoods(num):
            goods = 0
            for i in range(1,num):
                goods += i
            return goods
        bads = findgoods(len(nums)) 
        vals = defaultdict(int)
        for i in range(len(nums)):
            vals[nums[i]-i] += 1
        for k,v in vals.items():
            bads -= findgoods(v)
        return bads
            
            
        