class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 1
        s = '/'
        while i < len(path):
            if path[i] == '/':
                if s[-1] != '/':
                    stack.append(s)
                    s = '/'
                i+= 1
            elif s[-1] == '/' and path[i] == '.':
                other_char = False
                while i < len(path) and path[i] != '/':
                    s += path[i]
                    if path[i] != '.':
                        other_char = True
                    i += 1
                if other_char or len(s) > 3:
                    stack.append(s)
                elif len(s) == 2:
                        pass
                elif len(s) == 3:
                    if stack:
                        stack.pop()
                s = '/'
                i += 1
            else:
                s += path[i]
                i += 1
        if len(s) > 1:
            stack.append(s)
        if not stack : return '/'
        return ''.join(stack)