class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for cur_log in logs:
            if cur_log == './':
                continue
            elif cur_log == '../':
                if stack:
                    stack.pop()
            else:
                stack.append(cur_log)
        return len(stack)
        