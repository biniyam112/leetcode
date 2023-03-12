class Solution:
    def smallestSubsequence(self, s: str) -> str:
         #to know if a character is going to come again
        rem = Counter(s)
        
        stack = []
        seen = set()
        
        for c in s:
            rem[c] -= 1
            if c in seen:
                continue
                
            while stack and stack[-1] > c and rem[stack[-1]] > 0:
                last = stack.pop()
                seen.remove(last)
                
            stack.append(c)
            seen.add(c)
        return ''.join(stack)
                        