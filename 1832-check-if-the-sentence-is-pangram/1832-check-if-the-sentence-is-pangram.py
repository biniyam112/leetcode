class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        visited = set()
        for c in sentence:
            visited.add(c)
        if len(visited) == 26:
            return True
        return False
        