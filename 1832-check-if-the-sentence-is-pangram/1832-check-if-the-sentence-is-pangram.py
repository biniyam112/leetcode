class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        indexes = [0] * 26
        for c in sentence:
            indexes[ord(c)-97] = 1
        if sum(indexes) == 26:
            return True
        return False
        