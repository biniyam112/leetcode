class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square = []
        i = 0
        j = len(nums)-1
        while i <= j:
            right = nums[j]**2
            left = nums[i]**2
            if  right > left:
                square.append(right)
                j-=1
            else:
                square.append(left)
                i+=1
        
        return square[::-1]
        