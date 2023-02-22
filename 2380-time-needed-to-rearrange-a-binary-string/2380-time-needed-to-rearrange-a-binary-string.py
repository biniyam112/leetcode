class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = [int(x) for x in s]
        days = 0
        while True:
            temp = s.copy()
            for i in range(1,len(s)):
                if s[i] and not s[i-1]:
                    temp[i-1],temp[i] = temp[i],temp[i-1]
            if temp == s:
                return days
            else:
                s = temp
                days += 1
            