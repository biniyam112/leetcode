class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = []
        for i in range(len(shifts)-1,0,-1):
            shifts[i-1] += shifts[i]
        for i in range(len(shifts)):
            cur = (shifts[i]+ord(s[i])-97) % 26 + 97
            ans.append(chr(cur))
        return ''.join(ans)
        
        