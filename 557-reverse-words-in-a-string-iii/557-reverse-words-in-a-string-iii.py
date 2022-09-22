class Solution:
    def reverseWords(self, s: str) -> str:
        i,j = 0,0
        s  = [x for x in s]
        while j <= len(s):
            if j == len(s) or s[j] == ' ':
                k = j
                j -= 1
                while i < j:
                    s[i],s[j] = s[j],s[i]
                    i += 1
                    j -= 1
                i,j = k+1,k
            j += 1
        return ''.join(s)
                
        