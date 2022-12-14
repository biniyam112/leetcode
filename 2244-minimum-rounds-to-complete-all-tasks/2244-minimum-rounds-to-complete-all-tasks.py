class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks = Counter(tasks)
        ans = 0
        for count in tasks.values():
            if count == 1:
                return -1
            ans += (count //3) + ((count%3) != 0)
        return ans