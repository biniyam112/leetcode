class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1)+len(s2):
            return False
        @cache
        def interleave(cur1,cur2):
            if cur1+cur2 == len(s3):
                return True
            res = False
            for i in range(cur1,len(s1)):
                if s1[i] == s3[i+cur2]:
                    res = res or interleave(i+1,cur2)
                else:
                    break
            for i in range(cur2,len(s2)):
                if s2[i] == s3[cur1+i]:
                    res = res or interleave(cur1,i+1)
                else:
                    break
            return res
        return interleave(0,0)
                    
            