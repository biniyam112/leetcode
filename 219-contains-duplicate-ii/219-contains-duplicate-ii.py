class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = defaultdict(int)
        i = 0
        j = 0
        while j < len(nums):
            if k < 0:
                count[nums[i]] -= 1
                i += 1
            count[nums[j]] += 1
            if count[nums[j]] > 1:
                return True
            j += 1
            k -= 1
            