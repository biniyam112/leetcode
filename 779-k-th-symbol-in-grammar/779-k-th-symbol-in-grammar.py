class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        opp = {'1':'0','0':'1'}
        def find(k,n):
            if n == 1:
                return '0'
            half = 2**(n-2)
            if k <= half:
                return find(k,n-1)
            else:
                return opp[find(k-half,n-1)]
        return int(find(k,n))