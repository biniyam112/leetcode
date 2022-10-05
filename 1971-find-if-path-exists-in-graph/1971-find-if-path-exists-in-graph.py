class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        path = defaultdict(list)
        for edge in edges:
            path[edge[0]].append(edge[1])
            path[edge[1]].append(edge[0])
        # print(path)
        visited_s = set()
        visited_d = set()
        def dfs_s(val):
            if val in visited_s:
                return False
            visited_s.add(val)
            if val == destination:
                return True
            found = False
            for child in path[val]:
                found = found or dfs_s(child)
            return found
    
        
            
        return dfs_s(source)
                
        