class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        total = sum(nums)
        def play(i=0,j=len(nums)-1):
            if i == j:
                return nums[i]
            left = nums[i]-play(i+1,j)
            right = nums[j]-play(i,j-1)
            return max(left,right)
        p1 = play()
        return p1 >= 0