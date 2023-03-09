class Solution:
    def monkeyMove(self, n: int) -> int:
        def recursion(n,start = False):
            if n == 0 or n == 1:
                return 2 ** n
            val = recursion(n//2)
            if n%2 == 0:
                if start:
                    return (val * val - 2) % (10**9 + 7)
                return (val * val) % (10**9 + 7)
            if start:
                return (2 * val * val - 2) % (10**9 + 7)
            return (2 * val * val) % (10**9 + 7)
        return recursion(n,True)