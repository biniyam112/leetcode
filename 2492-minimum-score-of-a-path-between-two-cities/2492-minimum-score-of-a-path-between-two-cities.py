class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = [[] for i in range(n+1)]
        visited = [False for i in range(n+1)]
        for i in roads:
            graph[i[0]].append(tuple(i[1:]))
            graph[i[1]].append((i[0],i[2]))
        # print(graph)
        lst = []
        def dfs(visited,graph,source,lst):
            visited[source]=True
            for i in graph[source]:
                lst.append(i[-1])
                if visited[i[0]]==False:
                    dfs(visited,graph,i[0],lst)
        dfs(visited,graph,1,lst)
        return min(lst)
                    
        
        
        
        