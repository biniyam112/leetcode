class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        mods = defaultdict(int)
        presum = [0]
        
        for val in nums:
            temp = presum[-1]+val
            presum.append(temp%k)
            ans += not presum[-1]
            ans += mods[presum[-1]]
            mods[presum[-1]] += 1
        return ans
            
        