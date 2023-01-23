class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # [trusts,is_trusted]
        relation = [[0,0] for _ in range(n)]
        for er,ee in trust:
            relation[er-1][0] = 1
            relation[ee-1][1] += 1
        for index,(trusts,trusted) in enumerate(relation):
            if trusts == 0 and trusted == n-1:           
                return index+1
        return -1
        