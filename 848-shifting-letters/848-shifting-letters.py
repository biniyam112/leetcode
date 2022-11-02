class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = deque()
        pre = 0
        # little bit improvement in the time compexity
        # do presum and shifting in on iteration
        for i in range(len(shifts)-1,-1,-1):
            shifts[i] += pre
            pre = shifts[i]
            cur = (shifts[i]+ord(s[i])-97)%26 + 97
            ans.appendleft(chr(cur))
        return ''.join(ans)
            
        # reverse presum
        for i in range(len(shifts)-1,0,-1):
            shifts[i-1] += shifts[i]
            
        # shift characters
        for i in range(len(shifts)):
            cur = (shifts[i]+ord(s[i])-97) % 26 + 97
            ans.append(chr(cur))
        return ''.join(ans)
        
        