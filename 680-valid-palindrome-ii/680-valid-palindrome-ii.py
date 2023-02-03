class Solution:
    def isPalindrome(self,s):
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        count  = 0
        while i < j:
            if s[i] != s[j]:
                res = False
                res = res or self.isPalindrome(s[i+1:j+1])
                res = res or self.isPalindrome(s[i:j])
                return res
            else:
                i += 1
                j -= 1
        return True
                
        
        
                