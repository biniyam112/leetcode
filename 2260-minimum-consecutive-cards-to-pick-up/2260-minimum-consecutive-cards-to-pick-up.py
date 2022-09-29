class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        visited = defaultdict(int)
        diff =  float('inf')
        for i in range(len(cards)):
            if cards[i] in visited:
                diff = min(diff,i-visited[cards[i]]+1)
            visited[cards[i]] = i
        if diff == float('inf'):
            return -1
        return diff
        