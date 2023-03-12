class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for val in num:
            while stack and val < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            if not stack and val == '0':
                continue
            stack.append(val)
        ans = ''
        for i in range(len(stack)-k):
            ans += stack[i]
        if not ans: return '0'
        return ans
            
        