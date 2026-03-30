class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_char_diff = defaultdict(int)
        odd_char_diff = defaultdict(int)

        for i,c in enumerate(s1):
            if i % 2 == 0:
                even_char_diff[c] += 1
            else:
                odd_char_diff[c] += 1
        
        for i,c in enumerate(s2):
            if i % 2 == 0:
                even_char_diff[c] -= 1
            else:
                odd_char_diff[c] -= 1

        for c,val in even_char_diff.items():
            if val != 0:
                return False
        for c,val in odd_char_diff.items():
            if val != 0:
                return False
        return True