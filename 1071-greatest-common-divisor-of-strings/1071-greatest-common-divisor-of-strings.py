class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
    
        ans = ''
        def findMatch(prefix):
            i = 0
            while i < min(len(str1),len(str2)):
                if str1[i:i+len(prefix)] != prefix or str2[i:i+len(prefix)] != prefix:
                    return False
                i += len(prefix)
        for i in range(min(len(str1),len(str2))):
            prefix = str1[:i+1]
            if findMatch(prefix):
                ans = prefix
        return prefix
            
        