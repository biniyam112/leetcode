class Solution:
    def sumZero(self, n: int) -> List[int]:
        total  = 0
        ans = []
        for i in range(n-1):
            ans.append(i+1)
            total += i+1
        ans.append(-total)
        return ans
        