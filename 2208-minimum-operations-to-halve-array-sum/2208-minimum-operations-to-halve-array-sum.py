class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        half = total /2
        for i,num in enumerate(nums):
            nums[i] = -num
            
        
        heapq.heapify(nums)
        ans = 0
        while total > half:
            val = heapq.heappop(nums)
            val /= 2
            heapq.heappush(nums,val)
            total += val
            ans += 1
        return ans