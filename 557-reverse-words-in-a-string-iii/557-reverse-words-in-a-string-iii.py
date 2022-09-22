class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        k = ''
        for w in s:
            k += w[::-1]
            k += ' '
        return k[:-1]
        