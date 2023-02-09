class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        uniqueCnt = 0
        counter = [0] * 20001

        
        st = 0
        ed = 0
        
        while st < n:
            if ed < n and uniqueCnt < k:
                counter[nums[ed]] += 1
                # new number added to range
                if counter[nums[ed]] == 1:
                    uniqueCnt += 1
                ed += 1
            elif uniqueCnt == k:
                ans += 1
                diff = ed+1
                # number already in range
                while diff <= n and counter[nums[diff-1]] > 0:
                    diff += 1
                    ans += 1
                counter[nums[st]] -= 1
                uniqueCnt -= (counter[nums[st]] == 0)
                st += 1
            else:
                counter[nums[st]] -= 1
                uniqueCnt -= (counter[nums[st]] == 0)
                st += 1

                    
        return ans
                
        
        