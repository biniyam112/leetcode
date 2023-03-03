class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if i+len(needle) <= len(haystack) and needle == haystack[i:i+len(needle)]:
                return i
        return -1
        