class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        queue = deque()
        for k in range(len(s)):
            if s[k] == s[0]:
                queue.append(k)
        
        i,j = 0,1
        pat = ''
        while j < len(s):
            # print(i,j)
            if s[i] == s[j]:
                if s[i:j] == pat:
                    i += len(pat)
                    j += len(pat)
                else:
                    pat += s[i]
                    i += 1
                    j += 1
            elif i == 0:
                j += 1
            else:
                pat = ''
                i = 0
                queue.popleft()
                if queue:
                    j = queue[0]
        # print(pat)
        return pat and s == pat * (len(s) // len(pat))        
        