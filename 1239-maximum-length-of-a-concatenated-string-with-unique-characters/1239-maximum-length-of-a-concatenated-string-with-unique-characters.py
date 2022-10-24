class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        def napsack(index,chars):
            nonlocal ans
            if index == len(arr):
                return len(chars)
            isFound = False
            word = arr[index]
            if len(set(word)) < len(word):
                isFound = True
            for c in word:
                if c in chars: isFound = True
            take = skip = 0
            if not isFound:
                for c in word:
                    chars.add(c)
                take = napsack(index+1,chars)
                for c in word:
                    chars.discard(c)
            skip = napsack(index+1,chars)
            return max(take,skip)
        return napsack(0,set())