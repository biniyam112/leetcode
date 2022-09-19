class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occur = set()
        for k,v in count.items():
            if v in occur:
                return False
            occur.add(v)
        return True
        