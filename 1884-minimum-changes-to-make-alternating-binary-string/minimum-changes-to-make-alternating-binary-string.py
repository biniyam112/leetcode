class Solution:
    def minOperations(self, s: str) -> int:
        cost = 0
        n = len(s)
        for i in range(n):
            cost += (i%2 != int(s[i])) # We think starting with 0 is the right way (same as modulo 0,1,0,...)
        return min(cost,n-cost)
        