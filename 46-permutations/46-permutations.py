class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def recursion(permutation):
            if len(permutation) == len(nums):
                ans.append(permutation)
                return
            for num in nums:
                if num not in permutation:
                    copy = permutation.copy()
                    copy.append(num)
                    recursion(copy)
        for num in nums:
            recursion([num])
        return ans
        