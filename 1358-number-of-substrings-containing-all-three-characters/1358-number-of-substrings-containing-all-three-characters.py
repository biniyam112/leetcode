class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = 0
        left = 0
        ans = 0
        chars = defaultdict(int)
        while i < len(s):
            chars[s[i]] += 1
            if len(chars) == 3:
                ans += left+1
                while chars[s[left]] > 1:
                    chars[s[left]] -= 1
                    left += 1
                    ans += 1
            i += 1
        return ans