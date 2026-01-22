class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        operations = 0
        while True:
            n = len(nums)
            nonDecreasing = True

            minSum = float('inf')
            minSumIndex = 0
            for i in range(1,n):
                if nums[i]+nums[i-1] < minSum:
                    minSum = nums[i]+nums[i-1]
                    minSumIndex = i
            
            for i in range(1,n):
                if nums[i-1] > nums[i]:
                    nonDecreasing = False
                    nums[minSumIndex] = minSum
                    nums.pop(minSumIndex-1)
                    operations += 1
                    break
            print(nums)

            if nonDecreasing:
                return operations