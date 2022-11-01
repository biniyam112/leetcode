class Solution:

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and sum([int(x) for x in bin(n)[2:]]) < 2
        
            