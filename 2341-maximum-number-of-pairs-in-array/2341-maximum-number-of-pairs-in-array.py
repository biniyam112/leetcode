class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ans = [0,0]
        nums = Counter(nums)
        for _,v in nums.items():
            ans[0] += v // 2
            if v % 2 == 1:
                ans[1] += 1
        return ans
        