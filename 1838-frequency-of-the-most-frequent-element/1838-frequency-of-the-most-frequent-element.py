class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i,j = 0,1
        freq = 1
        nums.sort()
        while j < len(nums):
            k -= (j-i)*(nums[j]-nums[j-1])
            
            #while kalche
            while j > i and k < 0:
                k += nums[j]-nums[i]
                i += 1
            freq = max(freq,j-i+1)
            j += 1
        return freq