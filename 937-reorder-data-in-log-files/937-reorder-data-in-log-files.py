class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        
        for log in logs:
            listLog = log.split()
            if not listLog[-1].isdigit():
                ident = listLog[0]
                content = listLog[1:]
                letters.append([ident,content])
            else:
                digits.append(log)
        letters = sorted(letters,key = lambda pair : (pair[1],pair[0]))
        ans = []
        # print(letters)
        for letter in letters:
            log = [letter[0],' '.join(letter[1])]
            ans.append(' '.join(log))
        for digit in digits:
            ans.append(digit)
        return ans
        