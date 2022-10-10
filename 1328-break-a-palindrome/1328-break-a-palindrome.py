class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = [x for x in palindrome]
        if len(palindrome) == 1:
            return ''
        i = 0
        while i < len(palindrome) and palindrome[i] == 'a':
            i += 1
        if len(palindrome)%2 == 1 and i == len(palindrome)//2 or i == len(palindrome):
            if palindrome[-1] == 'a':
                palindrome[-1] = 'b'
            else:
                palindrome[-1] = 'a'
            return ''.join(palindrome)
        palindrome[i] = 'a'
        # return palindrome
        return ''.join(palindrome)