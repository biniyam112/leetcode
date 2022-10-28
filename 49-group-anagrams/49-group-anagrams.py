class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for index,word in enumerate(strs):
            groups[''.join(sorted(word))].append(index)
        ans = []
        for indices in groups.values():
            group = []
            for index in indices:
                group.append(strs[index])
            ans.append(group)
        return ans
        