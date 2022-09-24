class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = 0
        pairs = defaultdict(int)
        for domino in dominoes:
            if (domino[0],domino[1]) in pairs or (domino[1],domino[0]) in pairs:
                if domino[0] != domino[1]:
                    counter += pairs[(domino[0],domino[1])]
                    counter += pairs[(domino[1],domino[0])]
                else:
                    counter += pairs[(domino[0],domino[1])]
            pairs[(domino[0],domino[1])] += 1
        return counter
            