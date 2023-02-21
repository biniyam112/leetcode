class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        relation = defaultdict(list)
        indegree = [0] * n
        
        for from_,to in edges:
            indegree[to] += 1
            relation[from_].append(to)
        
        ans = []
        for i,count in enumerate(indegree):
            if not count: ans.append(i)
        return ans
            
        