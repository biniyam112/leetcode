class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = []
        idx = 0
        for idx in range(min(len(word1),len(word2))):
            final.append(word1[idx])
            final.append(word2[idx])
        final = ''.join(final)
        final += word1[idx+1:]
        final += word2[idx+1:]
        return final