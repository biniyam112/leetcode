class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def cleanUp(i=0,open_=0):
                if i == len(s):
                    return not open_
                if not open_ and s[i] == ')':
                    return False
                if s[i] == '(':
                    return cleanUp(i+1,open_+1)
                elif s[i] == ')':
                    return cleanUp(i+1,open_-1)
                else:
                    asOpen = cleanUp(i+1,open_+1)
                    asClose = open_ and cleanUp(i+1,open_-1)
                    asEmpty = cleanUp(i+1,open_)
                    return asOpen or asClose or asEmpty
        
        return cleanUp()