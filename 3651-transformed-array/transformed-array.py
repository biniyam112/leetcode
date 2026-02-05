class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        results = [x for x in nums]
        n = len(nums)

        for i in range(n):
            movement = (i+nums[i]) % n
            results[i] = nums[movement]
        
        return results


        