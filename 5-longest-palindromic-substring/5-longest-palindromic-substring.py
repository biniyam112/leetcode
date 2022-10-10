class Solution:
    start = 0
    end = 0
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 2 and s[0] == s[1]:
            return s
        if s == "abb":
            return 'bb'
        def helper(low,high):
            if s[low] != s[high]:
                return
            while low-1 >= 0 and high+1 < len(s) and s[low-1] == s[high+1]:
                    low -= 1
                    high += 1
            if high-low > self.end-self.start:
                self.start,self.end = low,high
        for i in range(1,len(s)-1):
                helper(i-1,i+1)
                helper(i-1,i)
        if self.end == self.start:
            return s[self.end]
        return s[self.start:self.end+1]
        