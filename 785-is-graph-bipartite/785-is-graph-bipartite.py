class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(val,cur):
            if cur == 'A':
                A.add(val)
            else:
                B.add(val)
            for negh in graph[val]:
                if negh not in A and negh not in B:
                    if cur == 'A':
                        dfs(negh,'B')
                    else:
                        dfs(negh,'A')
                
        A = set()
        B = set()
        for i in range(len(graph)):
            if i not in A and i not in B:
                dfs(i,'A')
        for i in range(len(graph)):
            for j in graph[i]:
                if i not in A and j not in A or i not in B and j not in B:
                    return False
        return True
        