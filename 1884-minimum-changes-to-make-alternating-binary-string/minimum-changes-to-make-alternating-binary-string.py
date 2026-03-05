class Solution:
    def minOperations(self, s: str) -> int:
        cost = [0,0]
        for i in range(len(s)):
            cost[0] += (i%2 != int(s[i])) # We think starting with 0 is the right way (same as modulo 0,1,0,...)
            cost[1] += (i%2 == int(s[i])) # We think starting with 1 is the right way (opposite to modulo 1,0,1,0...)
        return min(cost)
        