class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def findMatch(haystack,needle,offset):
            for i in range(len(needle)):
                if i+offset == len(haystack) or needle[i] != haystack[i+offset]:
                    return False
            return True
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if findMatch(haystack,needle,i):
                    return i
        return -1
        