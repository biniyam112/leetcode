class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(num):
            stack = []
            res = ''
            for val in num:
                if not stack or stack[-1] == val:
                    stack.append(val)
                else:
                    res += str(len(stack))+stack[-1]
                    stack = [val]
            res += str(len(stack))+stack[-1]
            return res
        
        def recursion(n,cur):
            if n == 0:
                return cur
            cur = helper(cur)
            return recursion(n-1,cur)
        return recursion(n-1,'1')
        