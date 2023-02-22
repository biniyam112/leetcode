class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = {}
        value = set()
        for i in range(len(s)):
            if (s[i] in mapper and mapper[s[i]] != t[i]):
                   return False
            elif s[i] not in mapper and t[i] in value:
                return False
            else:
                mapper[s[i]] = t[i]
                value.add(t[i])
        return True