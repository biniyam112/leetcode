class Solution:
    def minimumDeletions(self, s: str) -> int:
        prevA = []
        aCount = 0
        bCount = 0
        
        for c in s:
            prevA.append(aCount)
            aCount += c == 'a'
            
        bCount = len(s) - aCount
        deletion = min(aCount,bCount)
        for i in range(len(s)):
            b_seen = i - prevA[i]
            a_then = aCount - prevA[i]
            deletion_at = b_seen + a_then
            deletion = min(deletion,deletion_at)
        return deletion
                
                

        