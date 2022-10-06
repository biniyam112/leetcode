class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        @cache
        def recursion(index):
            if index == len(s):
                return 1
            if index > len(s):
                return 0
            if s[index] == '0':
                return 0
            one_step = 0
            two_steps = 0
            if index+2 <= len(s) and int(s[index:index+2]) <= 26:
                two_steps = recursion(index+2)
            one_step = recursion(index+1)
            return one_step+two_steps
        return recursion(0)