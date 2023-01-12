class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        
        ans = 0
        for _ in range(k):
            val = heapq.heappop(nums)
            ans -= val
            val = math.floor(val/3)
            heapq.heappush(nums,val)
        return ans