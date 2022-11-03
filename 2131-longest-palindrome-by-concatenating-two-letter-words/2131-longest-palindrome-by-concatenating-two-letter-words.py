class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        def isPalindrome(word):
            return word[0] == word[1]
        
        ans = 0
        arsenal = defaultdict(int)
        for word in words:
            arsenal[word] += 1
        
        visited = set()
        odd = False
        for k,v in arsenal.items():
            rev = k[::-1]
            if rev in arsenal and rev not in visited:
                if rev == k:
                    if v % 2 == 0:
                        ans += 2 * v
                    else:
                        ans += 2 * (v//2) * 2
                        odd = True
                else:
                    ans += 2 * 2 * min(v,arsenal[rev])
                    visited.add(k)
                
        return ans + odd*2
            
            