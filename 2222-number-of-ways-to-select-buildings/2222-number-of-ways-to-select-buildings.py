class Solution:
    def numberOfWays(self, s: str) -> int:
        freq = []
        n = len(s)
        s = [int(x) for x in s]
        counter = [0,0]
        for i in range(n):
            val = s[i]
            counter[val] += 1
            freq.append(counter.copy())
        totalOnes = sum(s)
        totalZeros = len(s)-totalOnes
        
        ans = 0
        for i in range(1,n):
            if s[i]:
                zerosBefore = freq[i-1][0]
                zerosAfter = totalZeros - zerosBefore
                ans += zerosBefore * zerosAfter
            else:
                onesBefore = freq[i-1][1]
                onesAfter = totalOnes - onesBefore
                ans += onesBefore * onesAfter
        return ans
            
            
        