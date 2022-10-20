class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(generated):
            stack = []
            i = 0
            while i < len(generated):
                if not stack and generated[i] == ')':
                    return False
                if generated[i] == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(generated[i])
                i += 1
            return not stack
        def getCombinations(combination):
            if len(combination) ==  n*2: 
                if isValid(combination):
                    ans.append(''.join(combination))
                return
            open_ = combination.copy()
            open_.append('(')
            close_ = combination
            close_.append(')')
            getCombinations(open_)
            getCombinations(close_)
        ans = []
        getCombinations([])
        return ans
                    
            