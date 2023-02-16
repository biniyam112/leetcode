class Solution:
    def romanToInt(self, s: str) -> int:
        valueMap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        intValue = 0
        x= len(s)-1
        while x>=0:
            if valueMap[s[x]] <= valueMap[s[x-1]] or x ==0:
                intValue+=valueMap[s[x]]
                x-=1
            else:
                intValue+= valueMap[s[x]] - valueMap[s[x-1]]
                x-=2
        return intValue
            