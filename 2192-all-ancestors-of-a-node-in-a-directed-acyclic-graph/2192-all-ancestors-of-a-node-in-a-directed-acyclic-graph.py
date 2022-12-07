class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        
        # get starting nodes
        starting_nodes = [1] * n
        for u,v in edges:
            starting_nodes[u] = 0
        # reversing the edges given
        for i in range(len(edges)):
            u,v =edges[i]
            edges[i] = [v,u]
        # building the reversed graph
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            
        def dfs(node):
            visited.add(node)
            for parent in graph[node]:
                ans[node].add(parent)
                if parent not in visited:
                    dfs(parent)
                for n in ans[parent]:
                    ans[node].add(n)
        
        visited = set()
        for i in range(n):
            if starting_nodes[i]: dfs(i)
        return [sorted(x) for x in ans]
        
        