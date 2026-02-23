class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        s = bin(n)[2:]
        last_idx = 0
        for i,c in enumerate(s):
            if c == '1':
                ans = max(ans,i-last_idx)
                last_idx = i
        return ans
        