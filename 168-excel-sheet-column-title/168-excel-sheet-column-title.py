class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        pad = 65
        while columnNumber:
            columnNumber -= 1
            mod = columnNumber % 26
            char = chr(mod+pad)
            columnNumber //= 26
            ans.append(char)
        # print(columnNumber)
        return ''.join(ans[::-1])
    
