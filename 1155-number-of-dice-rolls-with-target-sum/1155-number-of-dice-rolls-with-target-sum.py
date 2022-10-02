class Solution:
    @cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 0:
            if target == 0:
                return 1
            return 0
        ways = 0
        for i in range(1,k+1):
            ways += self.numRollsToTarget(n-1,k,target-i)
        return ways % (10**9+7)