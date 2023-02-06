class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words,key=lambda x: len(x))        
        chains = {}
        ans = 0

        for word in words:
            curMax = 0
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in chains:
                    curMax = max(curMax, chains[prev])
            chains[word] = 1 + curMax
            ans = max(ans, chains[word])
        return ans