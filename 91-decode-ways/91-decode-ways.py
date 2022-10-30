class Solution:
    def numDecodings(self, s: str) -> int:
        # dp recursive
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

        # dp iterative
        if s[0]=="0":
            return 0
        dp=[1, 1]
        prev=s[0]
        for each in s[1:]:
            result=0
            if each!="0":
                result+=dp[-1]
            if prev!="0" and int(prev+each)<=26:
                result+=dp[-2]
            dp.append(result)
            prev=each
        return dp[-1]