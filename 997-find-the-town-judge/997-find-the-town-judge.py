class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # [trusts,is_trusted]
        relation = [[0,0] for _ in range(n)]
        for er,ee in trust:
            relation[er-1][0] = 1
            relation[ee-1][1] += 1
        for i in range(n):
            if relation[i][0] == 0 and relation[i][1] == n-1:           
                return i+1
        return -1
        