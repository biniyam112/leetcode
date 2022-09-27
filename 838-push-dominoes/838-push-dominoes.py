class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = [x for x in dominoes]
        i = 0
        while i < len(dominoes):
            # print(i,dominoes[i])
            if dominoes[i] == 'R':
                r = i
                i += 1
                while i < len(dominoes) and dominoes[i] != 'L' and dominoes[i] != 'R':
                    i += 1
                if i == len(dominoes) or dominoes[i] == 'R':
                    while r < i:
                        dominoes[r] = 'R'
                        r += 1
                else:
                    l = i
                    r += 1
                    l -= 1
                    while r < l:
                        dominoes[r] = 'R'
                        dominoes[l] = 'L'
                        r += 1
                        l -= 1
                    i += 1
            elif dominoes[i] == 'L':
                cur = l = i
                i -= 1
                while i > -1 and dominoes[i] != 'R' and dominoes[i] != 'L':
                    i -= 1
                if i == -1 or dominoes[i] == 'L':
                    while l > i:
                        dominoes[l] = 'L'
                        l -= 1
                    i = cur+1
                else:
                    r = i
                    r += 1
                    l -= 1
                    while r < l:
                        dominoes[r] = 'R'
                        dominoes[l] = 'L'
                        r += 1
                        l -= 1
                i = cur+1
            else:
                i += 1
                
        return ''.join(dominoes)
            